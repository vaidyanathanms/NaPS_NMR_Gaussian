#!/bin/bash
#SBATCH --job-name G16_test
#SBATCH --nodes=1
#SBATCH --time=1:00:00
#SBATCH --account=synthesis
#SBATCH --error=std.err_%j
#SBATCH --output=std.out_%j
#SBATCH --exclusive
#SBATCH -p debug

# Load Gaussian module to set environment
module load gaussian python


cd $SLURM_SUBMIT_DIR
echo $PWD
INPUT_BASENAME=comp_nmr
GAUSSIAN_EXEC=g16

# Run gaussian NREL script (performs much of the Gaussian setup)
g16_nrel

#Setup Linda parameters
if [ $SLURM_JOB_NUM_NODES -gt 1 ]; then 
export GAUSS_LFLAGS='-vv -opt "Tsnet.Node.lindarsharg: ssh"' 
export GAUSS_EXEDIR=$g16root/g16/linda-exe:$GAUSS_EXEDIR 
fi 

# Run Gaussian job 
$GAUSSIAN_EXEC < $INPUT_BASENAME.com >& $INPUT_BASENAME.log 

echo "Completed successfully .. :)"
