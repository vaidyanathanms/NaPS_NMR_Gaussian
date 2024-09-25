# Generic Function Definitions
# Version_1: V_Sept_04_2024

import numpy as np
import os
import shutil
import subprocess
import sys
import glob
import re
import xml.etree.ElementTree as ET # For reading Avogadro cml/xml files

#---Generic function to copy files with *different* src/dest names
def my_cpy_generic(srcdir,destdir,inpfylname,destfylname):
    src_fyl  = srcdir  + '/' + inpfylname
    dest_fyl = destdir + '/' + destfylname
    shutil.copy2(src_fyl, dest_fyl)

#---Generic function to copy files with *same* src/dest names
def cpy_main_files(dum_maindir,dum_destdir,fylname):

    srcfyl = dum_maindir + '/' + fylname

    if not os.path.exists(srcfyl):
        print('ERROR', srcfyl, 'not found')
        return

    desfyl = dum_destdir + '/' + fylname
    shutil.copy2(srcfyl, desfyl)

#---Function to find all initital structures with cml extension
def find_inp_files(init_dir, inpstruct = 'all'):

    if not os.path.isdir(init_dir):
        raise RuntimeError(init_dir + " not found!")

    if isinstance(inpstruct,str):
        if inpstruct == 'all':
            inplist = glob.glob(init_dir + '/*.cml') 
            if inpstruct == []:
                raise RuntimeError('No cml input files found in ' + init_dir)
        else:
            if not os.path.exists(init_dir + '/' + inpstruct + '.cml'):
                raise RuntimeError(inpfyle + ' not found in ' + init_dir)
            inplist = [init_dir + '/' + inpstruct + '.cml']
    elif isinstance(inpstruct,list):
        inplist = []
        for structname in inpstruct:                
            fpath = init_dir + '/' + structname + '.cml'
            if not os.path.exists(fpath):
                print('ERROR', fpath, 'not found')
            else:
                inplist.append(fpath)
        if inplist == []:
             raise RuntimeError('No specified input cml found in '\
                                + init_dir)
    else:
        raise RuntimeError('Unknown type for spec_struct variable')
    
    return inplist

#---Edits headers of Gaussian i/p & adds coordinates to the files
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

#---Functiont to obtain charges from filename
#---Filename should be of the form *_qxm_*.cml where x is the charge
#---and m is optional for minus (negative) charges
def get_charges_from_fname(inpname):
    str_main = inpname.split('_')
    q_strarr = [[i,x] for i,x in enumerate(str_main) if x.startswith('q')]
    if len(q_strarr) == 0:
        raise RuntimeError('Input file format should have *_qxy_* in' \
                           'its filename and should repeat ONLY once!')
    for q_str in q_strarr:
        if q_str[0] == 0: continue # can be the naming
        qval = int(re.findall(r'\d+', q_str[1])[0])
        qval = -qval if 'm' in q_str[1] else qval
    return(qval)

#---Function to edit job submission files and submit jobs
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
    
#---Function to clean and backup files after generating i/p
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
            
#---Function to find recent file 
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

#---Function to create files to write outputs and headers
def gen_output_files(outdir,nmr_elem='None', flag_nmr = 0,\
                     flag_freq = 0, flag_nbo = 0):

    if nmr_elem == 'None':
        raise RuntimeError('ERROR: No reference for NMR analysis')
    
    fid_nmr = 0; fid_freq = 0; fid_nbo = 0

    if flag_nmr:
        fylename = set_filename(outdir, nmr_elem +'_nmr_output','csv')
        fid_nmr  = open(fylename,'w')
        fid_nmr.write('%s, %s, %s, %s,  %s, %s' %('Structure','NRef_Cntrs',\
                                                  'NMR_Freqs','NMR_FreqAvg',\
                                                  'NMR_Shifts','NMR_ShiftAvg'))
    if flag_freq:
        fid_freq = open(outdir + '/freq_analysis.dat','w')
    if flag_nbo:
        fid_nbo  = open(outdir + '/freq_analysis.dat','w')
    return fid_nmr, fid_freq, fid_nbo

#---Function to set the filenames depending upon what is already there
# in the directory
def set_filename(dirname, fileroot, fmt='csv'):
    fnames = dirname + '/' + fileroot + '.' + fmt
    if glob.glob(fnames) == []:
        return flist

    froots  = [item.replace('.csv','') for item in glob.glob(fnames)]
    root_id = [item.split('_')[-1] for item in froots if '_' in item]
    num_ids = [int(item) for item in root_id if item.isdigit()]
    if num_ids:
        return dirname + '/' + fileroot + '_' + str(max(num_ids)+1) +\
            '.' + fmt
    else:
        return dirname + '/' + fileroot + '_1.' + fmt
        
#---Function to compute the nmr frequency of the reference solution
def compute_refzero_nmr(solvdir,log_file,nmr_ref_elem):
    # Open file and process each line
    value = 0; cnt = 0
    with open(log_file,'r') as flog_id:
        for line in flog_id:
            line = line.strip()
            if 'isotropy' in line and line.split()[1] == nmr_ref_elem:
                value += float(line.split()[4]); cnt += 1

    if cnt == 0:
        return -1
    return float(value/cnt)

#---Write NMR outputs to file
def write_nmr_outputs(fid_nmr,nmrvals,ref_nmrfreq,fshift):
    if len(nmrvals) == 0:
        fid_nmr.write(f'{len(nmrvals)} , Results not converged\n')
    else:
        fid_nmr.write(f'{len(nmrvals)} ,') #Avg
        fid_nmr.write(" , ".join([str(value) for value in nmrvals]))
        fid_nmr.write(f', {sum(nmrvals)/len(nmrvals)} ,') #Avg
        if fshift:
            fid_nmr.write(" , ".join([str(ref_nmrfreq - value) \
                                     for value in nmrvals]))
            fid_nmr.write(' , %g\n' %(np.sum(ref_nmrfreq - \
                                             np.array(nmrvals))/len(nmrvals)))
            
        
#---Function to check log files are present in the directory 
def is_logfile(destdir):

    log_file = glob.glob(destdir + '/*.log')
    if log_file == []:
        return 'False'
    elif len(log_file) == 1:
        return log_file[0]
    else:
        return max(log_file,key=os.path.getctime)

#---Close all output files
def close_all_outfiles(flag_nmr, fid_nmr, flag_freq, fid_freq, \
                       flag_nbo, fid_nbo):
    if flag_nmr: fid_nmr.close()
    if flag_freq: fid_freq.close()
    if flag_nbo: fid_nbo.close()

 
