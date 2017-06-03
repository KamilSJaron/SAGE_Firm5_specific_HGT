#!/bin/bash
# -*- coding: utf-8 -*-
"""
Created on Thu May 23 2017

@author: Claivaz & Ricci

SCRIPT 8

align_potential_HGT.sh aligns the sequence of every blast hits of selected 
Gene_family_*_parsed.out (listed in list_files_HGT_to_trees.txt) in its created folder of group of bees 
(data/phylogeny_potential_HGT/Bumble_bees_proteins/, 
data/phylogeny_potential_HGT/Honey_bees_proteins/, 
data/phylogeny_potential_HGT/Bumble_Honey_bees_proteins/).

Inputs: amino_acid_seq_Gene_family_*_parsed.fasta in data/phylogeny_potential_HGT/protein_seq/

Outputs: Gene_family_*_parsed.multifasta in its corresponding folder of group of bees 
(data/phylogeny_potential_HGT/Bumble_bees_proteins/, 
data/phylogeny_potential_HGT/Honey_bees_proteins/, 
data/phylogeny_potential_HGT/Bumble_Honey_bees_proteins/) - each output file contains 
aligned protein sequences of every blast hits of a selected gene family
"""

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
	mkdir -p ./data/phylogeny_potential_HGT/$dir
done


for dir_file in $(cat ./data/parsed_blast/list_files_HGT_to_trees.txt); do
	INPUT=./data/phylogeny_potential_HGT/protein_seq/amino_acid_seq_$(basename ${dir_file%.out}).fasta
	OUTPUT=./data/phylogeny_potential_HGT/${dir_file%.out}.multifasta
	#echo $INPUT $OUTPUT
	mafft --auto $INPUT > $OUTPUT

done
