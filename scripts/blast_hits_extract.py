#!/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 2 14:10:31 2017

@author: Claivaz & Ricci

SCRIPT 4

For every blast results of each reference_genome|protein_ID’s sequence (query) present in 
each Gene_family_*.out files in each folder of group of bees (data/blast/Bumble_bees_proteins/, 
data/blast/Honey_bees_proteins/, data/blast/Bumble_Honey_bees_proteins/), blast_hits_extract.py 
parses hits according to different parameters (threshold_alignment_length, threshold_ID, 
threshold_eval, threshold_bitscore): 

threshold_alignment_length : constant = 0.8
threshold_ID : starts at 50
threshold _eval : 0.00001
threshold_bitscore : 0

For a given Gene_family_*.out, if there are less than 25 blast hits with parameters below, 
we relax the threshold_ID by multiplying it by 0.8 until reaching at least 25 blast hits 
(no hits with threshold_ID smaller than 20%). 
blast_hits_extract.sh creates output folders (data/parsed_blast/Bumble_bees_proteins/, 
data/parsed_blast/Honey_bees_proteins/, data/parsed_blast/Bumble_Honey_bees_proteins/) 
and assigns parameters as below.

Inputs: outputs of blast_gene_families.sh and function_blast.sh - Gene_family_*.out in 
data/blast/Bumble_bees_proteins/, data/blast/Honey_bees_proteins/, 
data/blast/Bumble_Honey_bees_proteins/ (to select Gene_family_*.out, blast_hits_extract.py 
will go through list_files.txt - created in the terminal: ls Gene_family_* > list_files.txt)

Outputs: Gene_family_*_parsed.out of its corresponding Gene_family_*.out of its corresponding 
folder of group of bees (data/blast/Bumble_bees_proteins/, data/blast/Honey_bees_proteins/, 
data/blast/Bumble_Honey_bees_proteins/) in its corresponding output folders 
(data/parsed_blast/Bumble_bees_proteins/, data/parsed_blast/Honey_bees_proteins/, 
data/parsed_blast/Bumble_Honey_bees_proteins/) - each Gene_family_*_parsed.out file contains 
the ‘best’ blast hits for each reference_genome|protein_ID’s sequence - the header is 
‘# Query_ID	Subject_titles	%_Identity	Alignment_length	evalue		bit_score’ 
- for each ‘best’ hits, informations are stored in its corresponding column
"""

# assigning the different input arguments to variables 
import sys, os

input_file = sys.argv[1]
bee_folder = sys.argv[2]
threshold_alignment_length = sys.argv[3]
threshold_ID = sys.argv[4]
threshold_eval = sys.argv[5]
threshold_bitscore = sys.argv[6]

# tmp_split_line[7] : query stop position
# tmp_split_line[6] : query start position
# tmp_split_line[9] : subject stop position
# tmp_split_line[8] : subject start position

# tmp_split_line[2] : % identity

# tmp_split_line[10] : E-value

# tmp_split_line[11] : BitScore

# tmp_split_line[0] : query ID
# tmp_split_line[13] : subject ID
# tmp_split_line[3] : Alignment length [bp]


### function to parse blast results
def parsed_blast_hits(input_file, bee_folder, threshold_alignment_length, threshold_ID, threshold_eval, threshold_bitscore):
    
    if input_file != 'list_files.txt': 
        bee_file = open('data/blast/' + bee_folder + '/' + input_file, 'r')
        bee_file_out = open('data/parsed_blast/' + bee_folder +'/' + input_file.split('.out')[0] + '_parsed.out','w')
        bee_file_out.write('# Query_ID\tSubject_titles\t%_Identity\tAlignment_length\tevalue\tbit_score\n')
        bee_file_list = []
        threshold_ID_tmp = float(threshold_ID)
        for line in bee_file:
            if '#' not in line:
                tmp_split_line = line.split('\t')
                if (float(tmp_split_line[7]) - float(tmp_split_line[6])) / (float(tmp_split_line[9]) - float(tmp_split_line[8])) >= float(threshold_alignment_length):
                    if float(tmp_split_line[2]) >= float(threshold_ID_tmp):
                        if float(tmp_split_line[10]) <= float(threshold_eval):
                            if float(tmp_split_line[11]) >= float(threshold_bitscore):
                                bee_file_list.append('%s\t%s\t%s\t%s\t%s\t%s\n'%(tmp_split_line[0], tmp_split_line[13].replace('.\n',''), tmp_split_line[2], tmp_split_line[3], tmp_split_line[10], tmp_split_line[11]))
        if len(bee_file_list) > 25:
            for blast_hit in bee_file_list:
                bee_file_out.write(blast_hit)
        elif float(threshold_ID_tmp) > 20: # decreasing threshold_ID by 80% until reaching 25 blast hits - no hits with threshold_ID lower than 20%
            bee_file_out.close()
            bee_file.close()
            parsed_blast_hits(input_file = input_file, bee_folder = bee_folder, threshold_alignment_length = threshold_alignment_length, threshold_ID = 0.8 * float(threshold_ID_tmp), threshold_eval = threshold_eval, threshold_bitscore = threshold_bitscore)
        else:
            for blast_hit in bee_file_list:
                bee_file_out.write(blast_hit)
        
            
        bee_file_out.close()
        bee_file.close()
            
parsed_blast_hits(input_file, bee_folder, threshold_alignment_length, threshold_ID, threshold_eval, threshold_bitscore)
