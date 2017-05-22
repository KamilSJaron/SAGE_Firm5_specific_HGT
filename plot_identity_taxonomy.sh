#!/bin/bash

#BSUB -L /bin/bash
#BSUB -o plot_identity_taxonomy.out
#BSUB -e plot_identity_taxonomy.err
#BSUB -J plot_identity_taxonomy
#BSUB -n 3
#BSUB -R "span[ptile=3]"
#BSUB -M 10000000
#BSUB –R "rusage[mem=10000]"
#BSUB -u virginie.ricci@unil.ch

module add R/3.3.2;

Rscript scripts/plot_identity_taxonomy.R
