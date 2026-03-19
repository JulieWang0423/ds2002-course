#!/bin/bash
#SBATCH --account=ds2002
#SBATCH --job-name=jobarray-book
#SBATCH --output=jobarray-book-%A-%a.out
#SBATCH --error=jobarray-book-%A-%a.err
#SBATCH --time=00:10:00
#SBATCH --partition=standard
#SBATCH --mem=8G
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=1
#SBATCH --array=1-5

INPUT=book-${SLURM_ARRAY_TASK_ID}.txt
OUTPUT=results-${SLURM_ARRAY_TASK_ID}.csv

python ~/ds2002-course/labs/07-hpc/process-book.py $INPUT $OUTPUT
