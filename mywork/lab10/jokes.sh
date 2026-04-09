#!/bin/bash
#SBATCH -A ds2002
#SBATCH -p standard
#SBATCH --array=1-10
#SBATCH -J lolcow_job
#SBATCH -o lolcow_%A_%a.out
#SBATCH -e lolcow_%A_%a.err
#SBATCH -t 00:01:00
#SBATCH --mem=8G
#SBATCH -n 1

module load apptainer
apptainer run lolcow-latest.sif
