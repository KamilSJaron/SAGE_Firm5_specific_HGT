#!/bin/bash
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 2017

@author: Claivaz & Ricci

SCRIPT 3.2

function_blast.sh creates output folders (data/blast/Bumble_bees_proteins, 
data/blast/Honey_bees_proteins, data/blast/Bumble_Honey_bees_proteins) and assigns 
variables used in blast_gene_families.sh (variables correspond to every 
Gene_family_*.fasta files present in each folder of group bees and stored in list_files.txt).

Inputs: outputs of proteinseqextract.py - Gene_family_*.fasta in data/Bumble_bees_proteins, 
data/Honey_bees_proteins, data/Bumble_Honey_bees_proteins (to select Gene_family_*.fasta, 
function_blast.sh will go through list_files.txt 
- created in the terminal: ls Gene_family_* > list_files.txt)

Outputs: Gene_family_*.out of its corresponding Gene_family_*.fasta of its corresponding 
folder of group of bees (data/Bumble_bees_proteins, data/Honey_bees_proteins, 
data/Bumble_Honey_bees_proteins) in its corresponding output folders 
(data/blast/Bumble_bees_proteins, data/blast/Honey_bees_proteins, 
data/blast/Bumble_Honey_bees_proteins) - each Gene_family_*.out file contains blast hits 
for each reference_genome|protein_ID’s sequence - for each reference_genome|protein_ID’s 
sequence (query): 5 first lines summarizing blastp information (version of BLASTP, query, 
database, fields and the total number of found hits) - fields correspond to the name of each 
resulting column (total of 14 columns) - subsequent lines correspond to every hits of the query
"""

for dir in Bumble_bees_proteins Bumble_Honey_bees_proteins Honey_bees_proteins; do

	for file in $(cat ./data/$dir/list_files.txt); do
		mkdir -p data/blast/$dir
		bash blast_gene_families.sh ./data/$dir/$file ./data/blast/$dir/$(basename $file .fasta).out
	done

done


