# -*- coding: utf-8 -*-
"""
Created on Tue May  2 14:10:31 2017

@author: Claivaz&Ricci

Script which filter the different hits from the blast output in function of different thresholds and the abscence of Lactobacillus in the strain subject
"""
import sys

input_file = sys.argv[1]
bee_folder = sys.argv[2]
threshold_alignment_length = sys.argv[3]
threshold_ID = sys.argv[4]
threshold_eval = sys.argv[5]
threshold_bitscore = sys.argv[6]

def parsed_blast_hits(input_file, bee_folder, threshold_alignment_length, threshold_ID, threshold_eval, threshold_bitscore):
    bee_file = open('data/blast/' + bee_folder + '/' + input_file, 'r')
    bee_file_out = open('data/parsed_blast/' + bee_folder +'/' + input_file.split('.out')[0] + '_parsed.out','w')
    bee_file_out.write('# Query_ID\tSubject_titles\t%_Identity\tAlignment_length\tevalue\tbit_score\n')
    for line in bee_file:
        if '#' not in line:
            tmp_split_line = line.split('\t')
            if (float(tmp_split_line[7]) - float(tmp_split_line[6])) / (float(tmp_split_line[9]) - float(tmp_split_line[8])) >= float(threshold_alignment_length):
                if float(tmp_split_line[2]) >= float(threshold_ID):
                    if float(tmp_split_line[10]) <= float(threshold_eval):
                        if float(tmp_split_line[11]) >= float(threshold_bitscore):
                            if 'Lactobacillus' not in tmp_split_line[13]:
                                bee_file_out.write('%s\t%s\t%s\t%s\t%s\t%s\n'%(tmp_split_line[0], tmp_split_line[13].replace('.\n',''), tmp_split_line[2], tmp_split_line[3], tmp_split_line[10], tmp_split_line[11]))
    
    bee_file_out.close()
    bee_file.close
        
parsed_blast_hits(input_file, bee_folder, threshold_alignment_length, threshold_ID, threshold_eval, threshold_bitscore)        
        
