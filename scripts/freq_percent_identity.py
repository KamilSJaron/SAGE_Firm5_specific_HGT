#!/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 2 14:10:31 2017

@author: Claivaz & Ricci

SCRIPT extra - cf. freq_precent_identity.R

freq_precent_identity.sh extracts every percent of identity values of every blast hits and stores
them

Inputs: outputs of blast_gene_families.sh and function_blast.sh - Gene_family_*.out in 
data/blast/Bumble_bees_proteins/, data/blast/Honey_bees_proteins/, 
data/blast/Bumble_Honey_bees_proteins/ (to select Gene_family_*.out, blast_hits_extract.py 
will go through list_files.txt - created in the terminal: ls Gene_family_* > list_files.txt)

Outputs: Percent_ID_list.txt in data/blast/ - listing all percent identity values of every blast hits
"""

import sys, os


def percent_identity_frequency(path_folder, list_files):

	output_fn = 'Percent_ID_list.txt'
	output_f = open('./data/blast/' + output_fn, 'w')

	percent_ID=[]


	folders_list = ['Bumble_bees_proteins', 'Honey_bees_proteins', 'Bumble_Honey_bees_proteins']

	for folder in folders_list:
		#os.chdir(path_folder + '/' + folder)
		
		files_list = open('./' + path_folder + '/' + folder + '/' + list_files, 'r')

		for files in files_list:
				file_f = open('./' + path_folder + '/' + folder + '/' + files.replace('\n',''), 'r')
			
				for line in file_f:
					if '#' not in line:
						lline = line.split()

						percent_ID.append(float(lline[2]))
				print('File done', files)

		print('Folder done', folder)
				
		for i in percent_ID:
			output_f.write('%f\n'%i)

	output_f.close()	



path_folder = sys.argv[1] # ./data/blast
list_files = sys.argv[2] # list_files.txt present in each bee folder


percent_identity_frequency(path_folder, list_files)