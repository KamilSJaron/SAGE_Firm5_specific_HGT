#!/bin/bash

#BSUB -L /bin/bash
#BSUB -o plot_identity_taxonomy.out
#BSUB -e plot_identity_taxonomy.err
#BSUB -J plot_identity_taxonomy
#BSUB -n 8
#BSUB -R "span[ptile=8]"
#BSUB -M 10000000
#BSUB –R "rusage[mem=10000]"
#BSUB -u virginie.ricci@unil.ch



python3 ./scripts/plot_identity_taxonomy.py ./data/parsed_blast/ Bumble_Honey_bees_proteins/Gene_family_1058_parsed.out hierarchical_taxonomy.txt

python3 ./scripts/plot_identity_taxonomy.py ./data/parsed_blast/ Bumble_bees_proteins/Gene_family_1674_parsed.out hierarchical_taxonomy.txt

python3 ./scripts/plot_identity_taxonomy.py ./data/parsed_blast/ Bumble_Honey_bees_proteins/Gene_family_83_parsed.out hierarchical_taxonomy.txt

python3 ./scripts/plot_identity_taxonomy.py ./data/parsed_blast/ Honey_bees_proteins/Gene_family_1393_parsed.out hierarchical_taxonomy.txt
