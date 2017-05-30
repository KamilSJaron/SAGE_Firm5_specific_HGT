#!/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 2017

@author: Claivaz & Ricci

SCRIPT 2

For each group of bees and for each Gene_family_*, proteinseqextract.py extracts all 
protein sequences for further ‘Blast’ step. This function creates a folder for each group 
of bees which comprises fasta files for each Gene_family_* containing protein sequences. 

Inputs: outputs of subgroup_sort.py in data/sort_group/ (Bumble_bees.txt, Honey_bees.txt, 
Bumble_Honey_bees.txt), all_proteins.fasta (in mls_2016/blast/) 

Outputs: folders in data/ of Bumble_bees_proteins, Honey_bees_proteins, 
Bumble_Honey_bees_proteins - each folder contains .fasta files of gene families 
(Gene_family_*.fasta) - a file concerns one gene family and contains all 
reference_genome|protein_ID and their sequence in fasta format

"""

from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
import os

### function to extract protein sequences
def extractprotseq(bee_group, bee_folder, all_proteins_faa):
	bee_group_f = open(bee_group, 'r')
	all_prot_f = open(all_proteins_faa, 'r')


	genome_protseq = {} # dico of ref_genome|protein_ID as keys and its amino acid sequence as values
	for seq_record in SeqIO.parse(all_prot_f, 'fasta'):
		genome_protseq[seq_record.id] = seq_record.seq


	for line in bee_group_f:
		lline = line.split()

		sequences = [] # list of ref_genome|protein_ID and its amino acid sequence of a Gene_family
		Gene_family = ''		
		Gene_family = lline[0]
		prot_seq_fn = Gene_family + '.fasta' #output names
		

		lline_wo_0 = lline[1::] # line without first element = Gene_family_*

		for obj in lline_wo_0:
			if obj in genome_protseq.keys():
				record = SeqRecord(genome_protseq[obj], id=obj)
				sequences.append(record)
			else:
				print('obj not found in all_prot_f', obj)
		SeqIO.write(sequences, bee_folder+prot_seq_fn, 'fasta')
		print(bee_group, '-', Gene_family, 'Done.')



### executing the function for the different group of bees
extractprotseq(bee_group = 'data/sort_group/Bumble_bees.txt', bee_folder = 'data/Bumble_bees_proteins/', all_proteins_faa = '/scratch/beegfs/monthly/mls_2016/blast/all_proteins.fasta')

extractprotseq(bee_group = 'data/sort_group/Honey_bees.txt', bee_folder = 'data/Honey_bees_proteins/', all_proteins_faa = '/scratch/beegfs/monthly/mls_2016/blast/all_proteins.fasta')

extractprotseq(bee_group = 'data/sort_group/Bumble_Honey_bees.txt', bee_folder = 'data/Bumble_Honey_bees_proteins/', all_proteins_faa = '/scratch/beegfs/monthly/mls_2016/blast/all_proteins.fasta')
