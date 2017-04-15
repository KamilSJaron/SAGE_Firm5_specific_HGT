#!/bin/bash

#BSUB -L /bin/bash
#BSUB -o proteinseqextract.out
#BSUB -e proteinseqextract.err
#BSUB -J proteinseqextract
#BSUB -n 8
#BSUB -R "span[ptile=8]"
#BSUB -M 10000000
#BSUB –R "rusage[mem=10000]"
#BSUB -u virginie.ricci@unil.ch


python3 proteinseqextract.py
