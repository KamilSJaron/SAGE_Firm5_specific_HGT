# -*- coding: utf-8 -*-
"""
Created on Tue May  2 14:10:31 2017

@author: Claivaz&Ricci
"""
import sys

input_file=sys.argv[1]
threshold_alignment_length=sys.argv[2]
threshold_ID=sys.argv[3]
threshold_eval=sys.argv[4]
threshold_bitscore=sys.argv[5]

def keep_hits(input_file, threshold_alignment_length, threshold_ID, threshold_eval, threshold_bitscore):
    bee_file=open(input_file, 'r')
    bee_file_out=open(input_file.split('.out')[0]+'_parsed.out','w')
    bee_file_out.write('# Query_ID\tSubject_titles\t%_Identity\tAlignment_length\tevalue\tbit_score\n')
    for line in bee_file:
        if '#' not in line:
            tmp_split_line = line.split('\t')
            if (float(tmp_split_line[7])-float(tmp_split_line[6]))/(float(tmp_split_line[9])-float(tmp_split_line[8]))>=threshold_alignment_length:
                if float(tmp_split_line[2]) >= threshold_ID:
                    if float(tmp_split_line[10]) <= threshold_eval:
                        if float(tmp_split_line[11]) >= threshold_bitscore:
                            if 'Lactobacillus' not in tmp_split_line[13]:
                                bee_file_out.write('%s\t%s\t%s\t%s\t%s\t%s\n'%(tmp_split_line[0],tmp_split_line[13],tmp_split_line[2],tmp_split_line[3],tmp_split_line[10],tmp_split_line[11]))
    
    bee_file_out.close()
    bee_file.close
        
keep_hits(input_file, threshold_alignment_length, threshold_ID, threshold_eval, threshold_biscore)        
        
