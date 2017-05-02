#!/bin/bash

#BSUB -L /bin/bash
#BSUB -o blast_hits_extract.out
#BSUB -e blast_hits_extract.err
#BSUB -J blast_hits_extract
#BSUB -n 8
#BSUB -R "span[ptile=8]"
#BSUB -M 10000000
#BSUB –R "rusage[mem=10000]"
#BSUB -u virginie.ricci@unil.ch


for dir in Bumble_bees_proteins Bumble_Honey_bees_proteins Honey_bees_proteins; do

	for file in $(cat ./data/blast/$dir/list_files.txt); do
		mkdir -p data/parsed_blast/$dir
		python3 scripts/blast_hits_extract.py $file $dir 1 60 0.00001 0 

	done
done


#input_file, bee_folder, threshold_alignment_length, threshold_ID, threshold_eval, threshold_biscore
