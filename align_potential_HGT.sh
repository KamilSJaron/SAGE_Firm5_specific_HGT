#!/bin/bash

#BSUB -L /bin/bash
#BSUB -o align_potential_HGT.out
#BSUB -e align_potential_HGT.err
#BSUB -J align_potential_HGT
#BSUB -n 3
#BSUB -R "span[ptile=3]"
#BSUB -M 10000000
#BSUB –R "rusage[mem=10000]"
#BSUB -u virginie.ricci@unil.ch


module add SequenceAnalysis/MultipleSequenceAlignment/mafft/7.305;

cd /scratch/beegfs/monthly/mls_2016/claivaz_ricci/SAGE_Firm5_specific_HGT/

for dir in Bumble_bees_proteins Bumble_Honey_bees_proteins Honey_bees_proteins; do
	mkdir -p ./data/alignment_potential_HGT/$dir
done


for dir_file in $(cat ./data/parsed_blast/list_files.txt); do
	INPUT=./data/parsed_blast/amino_acid_seq_$(basename ${dir_file%.out}).fasta
	OUTPUT=./data/alignment_potential_HGT/${dir_file%.out}.multifasta
	#echo $INPUT $OUTPUT
	mafft --auto $INPUT > $OUTPUT

done
