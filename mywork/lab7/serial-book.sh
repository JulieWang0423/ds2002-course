#!/bin/bash
#SBATCH --account=ds2002
#SBATCH --job-name=serial-book
#SBATCH --output=serial-book-%j.out
#SBATCH --error=serial-book-%j.err
#SBATCH --time=00:10:00
#SBATCH --partition=standard
#SBATCH --mem=8G
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=1
