#!/bin/bash
#SBATCH --job-name py_jname
#SBATCH --nodes=py_nnodes
#SBATCH --ntasks-per-node=py_ncores
#SBATCH --time=py_nhrs:00:00
#SBATCH --account=synthesis
#SBATCH --error=std.err_%j
#SBATCH --output=std.out_%j
#SBATCH -p debug

# Load Gaussian module to set environment
module load gaussian python

cd $SLURM_SUBMIT_DIR
echo $PWD

# Run gaussian NREL script (performs much of the Gaussian setup)
g16_nrel

#Setup Linda parameters
if [ $SLURM_JOB_NUM_NODES -gt 1 ]; then 
   export GAUSS_LFLAGS='-vv -opt "Tsnet.Node.lindarsharg: ssh"' 
   export GAUSS_EXEDIR=$g16root/g16/linda-exe:$GAUSS_EXEDIR 
fi 

# Run Gaussian job 
g16 < optim.com >& optim.log 
wait
g16 < optim2.com >& optim2.log 
wait
g16 < compnmr.com >& compnmr.log
wait

echo "Completed successfully .. :)"
