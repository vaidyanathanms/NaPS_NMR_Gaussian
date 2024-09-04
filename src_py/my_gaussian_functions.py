# Generic Function Definitions
# Version_1: V_Sept_04_2024

import numpy
import os
import shutil
import subprocess
import sys
import glob
import re
import xml.etree.ElementTree as ET # For reading Avogadro cml/xml files

def my_cpy_generic(srcdir,destdir,inpfylname,destfylname):
    src_fyl  = srcdir  + '/' + inpfylname
    dest_fyl = destdir + '/' + destfylname
    shutil.copy2(src_fyl, dest_fyl)

def cpy_main_files(dum_maindir,dum_destdir,fylname):

    srcfyl = dum_maindir + '/' + fylname

    if not os.path.exists(srcfyl):
        print('ERROR', srcfyl, 'not found')
        return

    desfyl = dum_destdir + '/' + fylname
    shutil.copy2(srcfyl, desfyl)

def find_inp_files(inpdir, inpfyle = 'all'):

    if not os.path.isdir(avog_dir):
        raise RuntimeError(avog_dir + " not found!")
    
    if inpfyle == 'all':
        inplist = glob.glob(avog_dir + '/*.cml')
        if inplist == []:
            raise RuntimeError('No input files found in ' + avog_dir)
    else:
        if not os.path.exists(avog_dir + '/' + inpfyle):
            raise RuntimeError(inpfyle + ' not found in ' + avog_dir)
        inplist = [avog_dir + '/' + inpfyle]
    return inplist

def edit_gen_inp_gauss_files(com_files,avog_inp_fyle,basis_fun='6-31G**',\
                             maxcycle=100,maxstep=30,solvent='water',\
                             scrf='pcm',multiplicity=1):

    # Obtain total charge from Avogadro file
    tree = ET.parse(avog_inp_fyle)  # Read XML data from file
    root = tree.getroot()
    totcharge = root.get('formalCharge')
    
    # Edit headers and options for calculations
    struct_name = avog_inp_fyle.split('.')[0]
    for fyle in com_files:
        fr  = open(fyle,'r')
        fw  = open(fyle.split('_')[0]+'.com','w')
        fid = fr.read().replace("py_basis",basis_fun)\
            replace("py_maxcyc",maxcycle)\
            replace("py_maxstep",maxstep)\
            replace("py_cavity",scrf)\
            replace("py_solv",solvent)\
            replace("py_struct",struct_name)\
            replace("py_charge",totcharge)\
            replace("py_mult",multiplicity)
        fw.write(fid)
        fr.close()

        for atom in root.find('atomArray').findall('atom'):
            element_type = atom.get('elementType')
            x3 = atom.get('x3')
            y3 = atom.get('y3')
            z3 = atom.get('z3')
        
            # Write in the format: elementType x3 y3 z3
            fw.write(f"{element_type} {x3} {y3} {z3}\n")

        fw.write('\n') # Extra line at the end

def run_gaussian(inpjob,structname,outjob='submit.sh',tot_hrs=1,\
                 tot_nodes=1,tot_cores=1):

    if not os.path.exists(inpjob):
        raise RuntimeError('ERROR: ' + inpjob + ' not found')
    
    jobstr = "job_" + structname
    fr  = open(inpjob,'r')
    fw  = open(outjob,'w')
    fid = fr.read().replace("py_jobname",jobstr).\
          replace("py_tottime",str(tot_hrs)).\
          replace("py_nnodes",str(tot_nodes)).\
          replace("py_ncores",str(tot_cores)).\
          replace("py_nptot",str(tot_cores*tot_nodes))
    fw.write(fid)
    fw.close()
    fr.close()

    subprocess.call(["sbatch", outjob])
    
    
def clean_backup_initfiles(destdir,structfile):
    
    initdir = destdir + '/init_files'
    if not os.path.isdir(initdir):
        os.mkdir(initdir)

    if os.path.exists(structfile):
        cpy_main_files(destdir,initdir,structfile)

    files = glob.glob('*var*')
    for fyl in files:
        if os.path.exists(fyl):
            cpy_main_files(destdir,initdir,fyl)
            os.remove(fyl)

def find_datafyle(nch_free,archstr,casenum,destdir):

    os.chdir(destdir)
    curr_dir = os.getcwd()
    datafyle = "PEdata_"+str(nch_free)+"_" +archstr+ \
               "_"+str(casenum)+".dat"

    if not os.path.exists(datafyle):
        print ("Data file not found ..")
        print ("Making datafile from restart files")
        restart_fyles = glob.glob('archival_*')
        
        if restart_fyles == []:
            return 'ERROR'

        if not os.path.exists('lmp_mesabi'):
        
            src_lmp = '/home/dorfmank/vsethura/mylammps/src/lmp_mesabi'
            destfyle = curr_dir + '/lmp_mesabi'
            shutil.copy2(src_lmp,destfyle)

        subprocess.call(['mpirun','-np','48','./lmp_mesabi','-r',restart_fyles[0],datafyle])
        
    return datafyle


def find_latest_trajfyle(pref,destdir):
    
    os.chdir(destdir)
    traj_arr = glob.glob(pref)
    if traj_arr == []:
        return 'ERROR'
    latest_fyle = max(traj_arr,key = os.path.getctime)
    return latest_fyle


def edit_generate_anainp_files(inpdata,inptraj,nch_tot,nch_free,\
                               nch_graft,cutoff,listnum):
    
    if not os.path.exists('anainp_var.txt'):
        print('ERROR: pe_params not found')
        return

    fr  = open('anainp_var.txt','r')
    outana = 'anainp_' + str(listnum) + '.txt'
    fw  = open(outana,'w')

    datafyle = re.split('/',inpdata)
    dataname = datafyle[len(datafyle)-1]

    trajfyle = re.split('/',inptraj)
    trajname = trajfyle[len(trajfyle)-1]
    

    fid = fr.read().replace("py_datafyl",dataname).\
          replace("py_trajfyl",trajname).\
          replace("py_ntotchains",str(nch_tot)).\
          replace("py_nfrchains", str(nch_free)).\
          replace("py_ngrchains",str(nch_graft)).\
          replace("py_cutoff",str(cutoff))
    fw.write(fid)
    fw.close()
    fr.close()

def run_analysis(nch_free,pdifree,casenum,dirstr,inpjob,outjob,listnum,destdir):

    if not os.path.exists(inpjob):
        print('ERROR: ', inpjob,'not found')
        return
    
    jobstr = "ana_" + str(nch_free) + "_" + str(pdifree) + "_" \
             + str(casenum) + "_" + dirstr
    fr  = open(inpjob,'r')
    fw  = open(outjob,'w')
    fid = fr.read().replace("py_jobname",jobstr).\
          replace("py_freech",str(nch_free)).\
          replace("py_pdifree",str(pdifree)).\
          replace("py_caselen",str(casenum)).\
          replace("pyfylval",str(listnum)).\
          replace("pyoutdir",str(destdir))
    fw.write(fid)
    fw.close()
    fr.close()

    subprocess.call(["qsub", outjob])


def find_recent_file(destdir,keyword): #A replica of find_recent_traj_file

    fylnames = destdir + '/' + keyword
    list_of_files = glob.glob(fylnames)
    if list_of_files != []:
        fyl_str = max(list_of_files, key=os.path.getctime)
        fyl_arr = fyl_str.split("/")
        print( "File Name: ", fyl_arr[len(fyl_arr)-1])
        return fyl_arr[len(fyl_arr)-1]
    else:
        return "nil"
    
