#!/bin/bash

#BSUB -L /bin/bash
#BSUB -o extract_taxonomy_hierarchy.out
#BSUB -e extract_taxonomy_hierarchy.err
#BSUB -J extract_taxonomy_hierarchy
#BSUB -n 8
#BSUB -R "span[ptile=8]"
#BSUB -M 10000000
#BSUB –R "rusage[mem=10000]"
#BSUB -u virginie.ricci@unil.ch



python3 ./scripts/extract_taxonomy_hierarchy.py
