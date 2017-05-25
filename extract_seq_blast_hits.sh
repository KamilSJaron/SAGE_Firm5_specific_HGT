#!/bin/bash

#BSUB -L /bin/bash
#BSUB -o extract_seq_blast_hits.out
#BSUB -e extract_seq_blast_hits.err
#BSUB -J extract_seq_blast_hits
#BSUB -n 3
#BSUB -R "span[ptile=3]"
#BSUB -M 10000000
#BSUB –R "rusage[mem=10000]"
#BSUB -u virginie.ricci@unil.ch


python3 ./scripts/extract_seq_blast_hits.py
