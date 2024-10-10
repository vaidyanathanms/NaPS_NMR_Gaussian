#----To analyze the log files from Gaussian outputs--------
#----Author: Vaidyanathan Sethuraman-----------------------
#----Date: Sept-01-2024------------------------------------
#----Requirements: my_gaussian_functions.py----------------

import numpy as np
import os
import shutil
import subprocess
import sys
import glob
from subprocess import call

#----my_gaussian_functions---------------------------------
from my_gaussian_functions import my_cpy_generic
from my_gaussian_functions import cpy_main_files
from my_gaussian_functions import is_logfile
from my_gaussian_functions import gen_output_files
from my_gaussian_functions import compute_refzero_nmr
from my_gaussian_functions import write_nmr_outputs
from my_gaussian_functions import close_all_outfiles

#----Input flags-------------------------------------------
flag_nmr   = 1  # Flag to compute NMR spectra
flag_shift = 1  # Flag to compute NMR shift
flag_freq  = 0  # Flag to process frequency
flag_nbo   = 0  # Flag to process NBO


nmr_ref_elem    = 'P' # Reference element for NMR spectra
nmr_refzero_dir = 'ref_H3PO4_q0' # Reference solution dir

#---------Input details------------------------------------
solv_arr     = ['Water','THF', 'DiethylEther', 'EthylEthanoate']
spec_struct  = ['u_P2S5_q0_1Sbridge','v_P2S10_q2m_endS3sym'\
                ,'w_P2S9_q2m_end2S3Sasym']
#spec_struct  = ['q_P2S6Na2_q0_cis','r_P2S6Na_qm1_1sodium',\
#                's_P2S8Na2_q0_cis','t_P2S8Na2_qm1_1sodium']

#---------Directory info---------------------------------------
maindir    = os.getcwd() #src_py dir
scratchdir = '/projects/iontransport' #output dir
scr_head   = 'naps_analysis' # head dir for scratch outputs

#---------Generate required output files-----------------------
workdir1 = scratchdir + '/' + scr_head   
if not os.path.isdir(workdir1):
    raise RuntimeError(workdir1 + " not found!")

if flag_nmr:
    ref_zero_head = workdir1 + '/' + nmr_refzero_dir
    if not os.path.isdir(ref_zero_head):
        raise RuntimeError(ref_zero_head + " not found!")
    

fid_nmr,fid_freq,fid_nbo = gen_output_files(workdir1,nmr_ref_elem,\
                                            flag_nmr,flag_freq,flag_nbo)

#---------Main analysis---------------------------------------

# Analyze for different solvents
for solvent in solv_arr:

    if flag_nmr:
        ref_zerosolv_dir = ref_zero_head + '/' + solvent
        if not os.path.isdir(ref_zerosolv_dir):
            print('ERROR: Reference solution directory for ' + \
                  solvent + ' not found!')
            fid_nmr.write(solvent + ' ref directory not found!')
            if flag_shift: continue

        log_file = is_logfile(ref_zerosolv_dir)
        if log_file == 'False':
            print('ERROR! No log files found in ' + ref_zerosolv_dir)
            fid_nmr.write(solvent + ' ref log file not found!')
            if flag_shift: continue
        
        ref_nmrfreq = compute_refzero_nmr(ref_zerosolv_dir,log_file,\
                                          nmr_ref_elem)
        if ref_nmrfreq == -1:
            print('Isotropy keyword found, but no values for: ' + \
                  nmr_ref_elem + ' in ' + ref_zerosolv_dir )
            if flag_shift: continue

        fid_nmr.write(f'\nNMR_Freq for reference in {solvent},'\
                      f'{ref_nmrfreq}\n')
            
    for structname in spec_struct:

        # Structure directory present
        workdir2  = workdir1 + '/' + structname
        if not os.path.isdir(workdir2):
            print('ERROR! ' + workdir2 + ' not found')
            continue
       
        # Check if destination directory is present
        workdir_main = workdir2 + '/' + solvent
        if not os.path.isdir(workdir_main):
            print('ERROR! ' + workdir_main + ' not found')
            continue

        # Check if Gaussian log file is present
        log_file = is_logfile(workdir_main)
        if log_file == 'False':
            print('ERROR! No log files found in ' + workdir_main)
            continue
            
        print('---Starting analysis for ' + structname + ' in '\
              +  solvent + '----')

        if flag_nmr:
            fid_nmr.write(f'{structname} ,')

        # Open file and process each line
        with open(log_file,'r') as flog_id:
            if flag_nmr: nmrvals = []
            for line in flog_id:
                line = line.strip()
                if flag_nmr and 'isotropy' in line and\
                   line.split()[1] == nmr_ref_elem:
                    nmrvals.append(float(line.split()[4]))

        # Average all values and write to outputs
        if flag_nmr: write_nmr_outputs(fid_nmr,nmrvals,ref_nmrfreq,\
                                       flag_shift)
        
#---Close all opened files    
close_all_outfiles(flag_nmr,fid_nmr, flag_freq,fid_freq, flag_nbo, fid_nbo)

print('Analysis completed :) ...')

