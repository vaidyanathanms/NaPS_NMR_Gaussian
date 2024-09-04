#----To copy NaPS structures from Avogadro output----------
#----To equilibrate and analyze NaPS structures------------
#----To analyze NMR spectra--------------------------------
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
from my_gaussian_functions import find_inp_files
from my_gaussian_functions import edit_gen_inp_gauss_files
from my_gaussian_functions import run_gaussian
from my_gaussian_functions import clean_backup_initfiles

#----Input flags-------------------------------------------
num_hrs   = 23 # Total number of hours for run
num_nodes = 1  # Number of nodes
num_cores = 32 # Number of cores per node

#---------Input details------------------------------------
basis_fun = 'UB3LYP/6-31+G(2df,p)'
maxcycle  = 200 # Max # of optim steps 
maxstep   = 10  # Max size for an optim step = 0.01*maxstep Bohr 
solv_arr  = ['water','THF','DME'] # THF, water (default), vacuum, DME
scrf      = 'pcm' # SCRF method pcm/smd
multiplicity = 1 # Multiplicity is 1 unless it is a radical
# Optional - if needed to specify one specific structure
#inpfyle   = 'all' # If specific structure, add here for analysis

#--------File lists--------------------------------------------
com_files = ['equil_var.com','equil2_var.com','comp_nmr_var.com']
sh_files  = ['gaussian_var.sh'] 

#---------Directory info---------------------------------------
maindir    = os.getcwd() #src_py dir
src_com    = '/home/vaidyams/all_codes/naps/src_com' #src_com dir
src_sh     = '/home/vaidyams/all_codes/naps/src_sh' #src_sh dir
avog_dir   = '/home/vaidyams/all_codes/naps/avog_dir' #inp guess
scratchdir = '/projects/synthesis' #output dir
gauss_exe  = 'g16' # lmp executable file
scr_head   = 'naps_analysis' # head dir for scratch outputs

#--------Find all/specific structure files-----------------------

inp_struct_list = find_inp_files(avog_dir, spec_str_flag)

#---------main analysis------------------------------------------
for structs in range(len(inp_struct_list)):

    workdir1 = scratchdir + '/' + scr_head   
    if not os.path.isdir(workdir1):
        os.mkdir(workdir1)

    avog_inp_fyle = os.path.basename(structs)
    avog_inp_root = avog_inp_fyle.split('.')[0]
    workdir2  = workdir1 + '/' + avog_inp_root
    if not os.path.isdir(workdir2):
        os.mkdir(workdir2)
	
    print("----Starting Gaussian calcs for " + avog_inp_root +\
          "-----")

    # Analyze for different solvents
    for solvent in solv_arr:

        workdir_main = workdir2 + '/' + solvent
        if not os.path.isdir(workdir_main):
            os.mkdir(workdir_main)

        print("Solvent: " + solvent)
            
        os.chdir(workdir_main)
        destdir = os.getcwd()
        print( "Current dir: ", destdir)
        
        #---Copying files------
        print( "Copying files")

        cpy_main_files(avog_dir,destdir,avog_inp_fyle)
                
        for fyllist in range(len(com_files)):
            cpy_main_files(src_com,destdir,com_files[fyllist])
        
        for fyllist in range(len(sh_files)):
            cpy_main_files(src_sh,destdir,sh_files[fyllist])

        #---Write headers to input files------
        print("Generating input Gaussian file")
        edit_gen_inp_gauss_files(com_files,avog_inp_fyle,basis_fun,\
                                 maxcycle,maxstep,solvent,scrf,multiplicity)


        #---Edit and submit gauss_var.sh----------------
        print("Editing and submitting submission script")
        run_gaussian(sh_files[0],avog_inp_root,'job_gauss.sh',num_hrs,\
                     num_nodes,num_cores)

        #---Cleaning up jobs----------------------------
        clean_backup_files(destdir,avog_inp_file)

        
    
