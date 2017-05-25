#!/bin/python3

import sys, os

from Bio import Entrez
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

import re

import random

Entrez.email = 'virginie.ricci@unil.ch'

os.chdir('data/parsed_blast/')


potential_HGT_dir_file_fn = 'list_files.txt'
potential_HGT_dir_file_f = open(potential_HGT_dir_file_fn, 'r')

list_HGT_dir_file=[] #ex: Bumble_Honey_bees_proteins/Gene_family_1058_parsed.out
for line in potential_HGT_dir_file_f:
	list_HGT_dir_file.append(line.replace('\n',''))


query_blast=[] #WP_****
for HGT in list_HGT_dir_file:

	HGT_str = str(HGT)
	parsed_blast_hits_f = open('./' + HGT_str, 'r')

	for line in parsed_blast_hits_f:
		if '#' not in line:
			lline = line.split()

			if lline[1].split('|')[1] not in query_blast:
				query_blast.append(lline[1].split('|')[1]) #WP_****

	dict_query_seq = {} # query as keys and amino acid seq as values
	dict_strain_query = {} # strain as keys and query as values
	for query in set(query_blast):
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
				
				if strain_ID in dict_strain_query.keys():
					dict_strain_query[strain_ID].append(query)
				else:
					dict_strain_query[strain_ID] = [query]


		aa_seq_tmp_wo_digits=[] #remove remained digits in aa sequence
		for s in aa_seq_tmp:
			if not s.isdigit():
				aa_seq_tmp_wo_digits.append(s)

		aa_seq = ''.join(aa_seq_tmp_wo_digits)
		dict_query_seq[query] = aa_seq
		#print(HGT, '\n', query, '\t', aa_seq, '\n')

	print(HGT, len(dict_strain_query.keys()), dict_strain_query)


	random.seed(123)
	if len(dict_query_seq.keys()) < 50:
		random_query_seq = random.sample(dict_query_seq.keys(), len(dict_query_seq.keys()))
	else: 
		random_query_seq = random.sample(dict_query_seq.keys(), 50)

	print('\n\nSELECTED', HGT, len(random_query_seq), random_query_seq, '\n\n')


	hierarchical_tax_f = open('hierarchical_taxonomy.txt', 'r')
	
	id_strain_query=[]
	for i in random_query_seq: # ex: ['WP_037591107', 'WP_001083113', ...]
		for obj in list(dict_strain_query.items()): # ex: ('Lactobacillus mali', ['WP_056991303', 'WP_003689228'])
			if i in obj[1]: 
				for line in hierarchical_tax_f:
					lline = line.split('\t')
					if lline[0] == i:
						id_strain_query.append(obj[0].replace(' ', '_').replace('[','').replace(']', '') + '_' + i + '_' + lline[2]) # obj[0]: ex: 'Lactobacillus mali', i: ex: WP_056991303, lline[2]: hierarchical distance
						# ex: Lactobacillus_mali_WP_056991303_3
	print(id_strain_query)


	sequences=[]
	for i in random_query_seq: # ex: ['WP_037591107', 'WP_001083113', ...]
		for j in id_strain_query: # ex: ['Streptococcus_anginosus_group_WP_037591107_3', 'Streptococcus_mitis_WP_001083113_3', ...]
			if i in j:
				record = SeqRecord(Seq(dict_query_seq[i]), id = j, description='')
				sequences.append(record)


# 	sequences=[]
# 	for i in random_query_seq:
# 		#print(HGT, '\n', i, '\t', dict_query_seq[i], '\n')
# 			record = SeqRecord(Seq(dict_query_seq[i]), id = i, description='')
# 			sequences.append(record)


	SeqIO.write(sequences, 'amino_acid_seq_' + HGT_str.replace('.out', '.fasta').split('/')[1], 'fasta')
		
	
