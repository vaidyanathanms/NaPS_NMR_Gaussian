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

def find_inp_files(init_dir, inpstruct = 'all'):

    if not os.path.isdir(init_dir):
        raise RuntimeError(init_dir + " not found!")

    if isinstance(inpstruct,str):
        if inpstruct == 'all':
            inplist = glob.glob(init_dir + '/*.cml') #Check cml files first
            if inpstruct == []:
                raise RuntimeError('No cml input files found in ' + init_dir)
        else:
            if not os.path.exists(init_dir + '/' + inpstruct):
                raise RuntimeError(inpfyle + ' not found in ' + init_dir)
            inplist = [init_dir + '/' + inpstruct]
    elif isinstance(inpstruct,list):
        inplist = []
        for fyle in inpstruct:                
            fpath = init_dir + '/' + fyle
            if not os.path.exists(fpath):
                print('ERROR', fpath, 'not found')
            else:
                inplist.append(fpath)
        if inplist == []:
             raise RuntimeError('No file in ' + inpstruct + \
                                ' found in ' + init_dir)
    else:
        raise RuntimeError('Unknown type for spec_struct variable')
    
    return inplist

def edit_gen_inp_gauss_files(com_files,inpfyle,basis_fun='6-31G**',\
                             maxcycle=100,maxstep=30,maxEstep=600,scrf='pcm',\
                             solvent='water',pop_style='reg',multiplicity=1):

    # Edit headers and options for calculations
    struct_name = inpfyle.split('.')[0] # Define structure name

    # Obtain total charge from Avogadro file or from filename
    tree = ET.parse(inpfyle)  # Read XML data from file
    root = tree.getroot()
    totcharge = root.get('formalCharge')
    if totcharge is None: totcharge=get_charges_from_fname(struct_name)
    print('Net_Charge: ', totcharge)

    # Edit com files
    for fyle in com_files:
        fr  = open(fyle,'r')
        fw  = open(struct_name + '_' + fyle.split('_')[0]+'.com','w')
        fid = fr.read().replace("py_basis",basis_fun)\
            .replace("py_maxcyc",str(maxcycle))\
            .replace("py_maxstep",str(maxstep))\
            .replace("py_maxEstep",str(maxEstep))\
            .replace("py_cavity",scrf)\
            .replace("py_solv",solvent)\
            .replace("py_popstyle",pop_style)\
            .replace("py_struct",struct_name)\
            .replace("py_charge",str(totcharge))\
            .replace("py_mult",str(multiplicity))
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

def get_charges_from_fname(inpname):
    str_main = inpname.split('_')
    q_str    = [x for x in str_main if x[0] == 'q']
    if len(q_str) != 1:
        raise RuntimeError('Input file format should have *_qxy_* in \
        its filename and should repeat ONLY once!')
    qval = int(re.findall(r'\d+', q_str[0])[0])
    qval = -qval if 'm' in q_str[0] else qval
    return(qval)
    
def run_gaussian(inpjob,structname,ginput='optim_var.com',\
                 outjob='submit.sh',tot_hrs=1,tot_nodes=1,tot_cores=1):

    if not os.path.exists(inpjob):
        raise RuntimeError('ERROR: ' + inpjob + ' not found')

    ginp_main = structname + '_' + ginput.split('_')[0]
    if not os.path.exists(ginp_main+'.com'):
        raise RuntimeError('ERROR: ' + ginp_main + ' not found')
        
    jobstr = structname
    fr  = open(inpjob,'r')
    fw  = open(outjob,'w')
    fid = fr.read().replace("py_jname",jobstr).\
          replace("py_tottime",str(tot_hrs)).\
          replace("py_nnodes",str(tot_nodes)).\
          replace("py_ncores",str(tot_cores)).\
          replace("py_ncores",str(tot_cores)).\
          replace("py_nptot",str(tot_cores*tot_nodes)).\
          replace("py_ginput",str(ginp_main))
    fw.write(fid)
    fw.close()
    fr.close()
    subprocess.call(["sbatch", outjob])
    
    
def clean_backup_initfiles(destdir,structfile):
    
    initdir = destdir + '/init_files'
    if not os.path.isdir(initdir):
        os.mkdir(initdir)

    print(structfile)
    if os.path.exists(structfile):
        cpy_main_files(destdir,initdir,structfile)

    files = glob.glob('*var*')
    for fyl in files:
        if os.path.exists(fyl):
            cpy_main_files(destdir,initdir,fyl)
            os.remove(fyl)

def find_recent_file(destdir,keyword): 

    fylnames = destdir + '/' + keyword
    list_of_files = glob.glob(fylnames)
    if list_of_files != []:
        fyl_str = max(list_of_files, key=os.path.getctime)
        fyl_arr = fyl_str.split("/")
        print( "File Name: ", fyl_arr[len(fyl_arr)-1])
        return fyl_arr[len(fyl_arr)-1]
    else:
        return "nil"
    
