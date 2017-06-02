#!/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 23 2017

@author: Claivaz & Ricci

SCRIPT 7


Manually, we decide which gene families are good candidates to investigate if orthologous 
genes are acquired by HGT. These gene family candidates are listed in list_files_HGT_to_trees.txt 
(in data/parsed_blast/). Gene_family_1058_parsed.out and Gene_family_991_parsed.out 
(data/parsed_blast/Bumble_Honey_bees_proteins/) correspond to ‘confirmed’ HGT candidates. 
Gene_family_1099_parsed.out (data/parsed_blast/Bumble_Honey_bees_proteins/) and 
Gene_family_1674_parsed.out (data/parsed_blast/Bumble_bees_proteins/) correspond to 
‘supposed’ HGT candidates. Gene_family_1048_parsed.out 
(data/parsed_blast/Bumble_Honey_bees_proteins/) corresponds to non-HGT candidate. 

extract_seq_blast_hits.py extracts the protein sequence of every blast hits of 
selected Gene_family_*_parsed.out (listed in list_files_HGT_to_trees.txt). 

Inputs: list_files_HGT_to_trees.txt in data/parsed_blast/, Gene_family_*_parsed.out of its corresponding 
folder of group of bees (data/parsed_blast/Bumble_bees_proteins/, 
data/parsed_blast/Honey_bees_proteins/, data/parsed_blast/Bumble_Honey_bees_proteins/) 
listed in list_files_HGT_to_trees.txt

Outputs: amino_acid_seq_Gene_family_*_parsed.fasta in data/alignment_potential_HGT/protein_seq/ - each output file 
contains protein sequences of every blast hits of a selected gene family. The ID name of 
each sequence is defined as follows: StrainName_SujectID_HierarchicalTaxonomyDistance
"""

import sys, os

from Bio import Entrez
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

import re

import random

Entrez.email = 'virginie.ricci@unil.ch'

os.chdir('data/parsed_blast/')


potential_HGT_dir_file_fn = 'list_files_HGT_to_trees.txt'
potential_HGT_dir_file_f = open(potential_HGT_dir_file_fn, 'r')

list_HGT_dir_file=[] # ex: Bumble_Honey_bees_proteins/Gene_family_1058_parsed.out
for line in potential_HGT_dir_file_f:
	list_HGT_dir_file.append(line.replace('\n',''))



for HGT in list_HGT_dir_file: # ex: Bumble_Honey_bees_proteins/Gene_family_1058_parsed.out
	orthologs=[] # ex: F225|1578.157.peg.1008
	query_blast=[] # WP_**** - blast hits

	HGT_str = str(HGT)
	parsed_blast_hits_f = open(HGT_str, 'r')

	for line in parsed_blast_hits_f:
		if '#' not in line:
			lline = line.split()

			if lline[0] not in orthologs:
				orthologs.append(lline[0])

			if lline[1].split('|')[1] not in query_blast:
				query_blast.append(lline[1].split('|')[1]) # WP_****

	# extracting protein sequences of query
	dict_query_seq = {} # query as keys and amino acid seq as values
	dict_strain_query = {} # strain as keys and query as values
	for query in query_blast:
		handle = Entrez.efetch(db="protein", id = query, rettype = "gb", retmode = "text")
	
		write_switch = False
		aa_seq_tmp = ''
		for line_handle in handle.readlines():
			if write_switch == True and '//' in line_handle: # '//' means the end of aa sequence
				aa_seq_tmp = aa_seq_tmp + line_handle
				aa_seq_tmp = aa_seq_tmp.replace(' ','').replace('\n','').replace('\t','').replace('.','').replace('//','')
				write_switch = False
			elif write_switch == True:
				aa_seq_tmp = aa_seq_tmp + line_handle
			elif 'ORIGIN' in line_handle:
				write_switch = True

			if re.match(r'^SOURCE', line_handle): # extract strain names, ex: Lactobacillus apis or Oceanobacillus sojae
				strain_ID = line_handle.replace('SOURCE      ', '').replace('\n', '')
				
				if strain_ID in dict_strain_query.keys(): # strain_ID already as keys
					dict_strain_query[strain_ID].append(query) # list of queries as values for a given key
				else:
					dict_strain_query[strain_ID] = [query]


		aa_seq_tmp_wo_digits=[] # remove remained digits in aa sequence
		for s in aa_seq_tmp:
			if not s.isdigit():
				aa_seq_tmp_wo_digits.append(s)

		aa_seq = ''.join(aa_seq_tmp_wo_digits)
		dict_query_seq[query] = aa_seq
		#print(HGT, '\n', query, '\t', aa_seq, '\n')

	print('\n\n', HGT, len(dict_strain_query.keys()), dict_strain_query)

	# randomly selecting 50 protein sequences (blast hits) of query for inferring phylogenetic trees
	random.seed(123)
	if len(dict_query_seq.keys()) < 50:
		random_query_seq = random.sample(dict_query_seq.keys(), len(dict_query_seq.keys()))
	else: 
		random_query_seq = random.sample(dict_query_seq.keys(), 50)

	print('\n\nSELECTED', HGT, len(random_query_seq), random_query_seq)

	# adding hierarchical taxonomy distance to blast hit labels
	hierarchical_tax_f = open('hierarchical_taxonomy.txt', 'r')
	
	id_strain_dist=[]
	for line in hierarchical_tax_f:
		lline = line.split()
		for i in random_query_seq: # ex: ['WP_037591107', 'WP_001083113', ...]
			if i == lline[0]:
				id_strain_dist.append(i + '_' + lline[2]) # ex: ['WP_037591107_3', 'WP_001083113_3', ...]

	print('\n\nID_STRAIN_DIST', id_strain_dist)

	# adding strain to blast hit labels
	id_strain_query=[]
	for i in id_strain_dist: # ex: ['WP_037591107_3', 'WP_001083113_3', ...]
		for obj in list(dict_strain_query.items()): # ex: ('Lactobacillus mali', ['WP_056991303', 'WP_003689228'])
			if '_'.join(i.split('_')[:-1]) in obj[1]:
				id_strain_query.append(obj[0].replace(' ', '_').replace('[','').replace(']', '').replace('(', '').replace(')', '') + '_' + i)

	print('\n\nID_STRAIN_QUERY', id_strain_query)


# 	id_strain_query=[]
# 	for i in random_query_seq: # ex: ['WP_037591107', 'WP_001083113', ...]
# 		for obj in list(dict_strain_query.items()): # ex: ('Lactobacillus mali', ['WP_056991303', 'WP_003689228'])
# 			for line in hierarchical_tax_f:
# 				lline = line.split()
# 				if i in obj[1] and i == lline[0]:
# 						id_strain_query.append(obj[0].replace(' ', '_').replace('[','').replace(']', '') + '_' + i + '_' + lline[2]) # obj[0]: ex: 'Lactobacillus mali', i: ex: WP_056991303, lline[2]: hierarchical distance
# 						# ex: Lactobacillus_mali_WP_056991303_3
	


	# extracting protein sequences of orthologs
	dict_orthologs_seq = {} # orthologs as keys and amino acid seq as values
	all_prot_f = '/scratch/beegfs/monthly/mls_2016/blast/all_proteins.fasta'
	ref_protseq = {} # dico of ref_genome|protein_ID as keys and its amino acid sequence as values
	for seq_record in SeqIO.parse(all_prot_f, 'fasta'):
		ref_protseq[seq_record.id] = seq_record.seq

	for ortho in orthologs:
		if ortho in ref_protseq.keys():
			dict_orthologs_seq[ortho] = ref_protseq[ortho]

	if len(dict_orthologs_seq.keys()) < 5:
		random_ref_protseq = random.sample(dict_orthologs_seq.keys(), len(dict_orthologs_seq.keys()))
	else:
		random_ref_protseq = random.sample(dict_orthologs_seq.keys(), 5)

	print('\n\nSELECTED_orthologs', len(random_ref_protseq), random_ref_protseq)

	# storing ref ortholog and its sequence in fasta format
	sequences=[]
	for i in random_ref_protseq:
		record = SeqRecord(ref_protseq[i], id = i, description='')
		sequences.append(record)			




	# storing blast hit label and its sequence in fasta format
	for i in random_query_seq: # ex: ['WP_037591107', 'WP_001083113', ...]
		for j in id_strain_query: # ex: ['Streptococcus_anginosus_group_WP_037591107_3', 'Streptococcus_mitis_WP_001083113_3', ...]
			if i in j:
				record = SeqRecord(Seq(dict_query_seq[i]), id = j, description='')
				sequences.append(record)


	SeqIO.write(sequences, '' + 'amino_acid_seq_' + HGT_str.replace('.out', '.fasta').split('/')[1], 'fasta')
		
	
	parsed_blast_hits_f.close()

potential_HGT_dir_file_f.close()
hierarchical_tax_f.close()