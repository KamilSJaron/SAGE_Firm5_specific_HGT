#!/bin/bash

#BSUB -L /bin/bash
#BSUB -o freq_percent_identity.out
#BSUB -e freq_percent_identity.err
#BSUB -J freq_percent_identity
#BSUB -n 3
#BSUB -R "span[ptile=3]"
#BSUB -M 10000000
#BSUB –R "rusage[mem=10000]"
#BSUB -u virginie.ricci@unil.ch


python3 ./scripts/freq_percent_identity.py data/blast list_files.txt

module add R/3.3.2;

Rscript ./scripts/freq_percent_identity.R
