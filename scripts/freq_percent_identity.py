#!/bin/python3

import sys, os
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
#import seaborn as sns
#sns.set()

def percent_identity_frequency(path_folder, list_files):

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
				

	plt.plot(percent_ID)
	plt.grid(True)
	plt.xlim(min(percent_ID)-1, max(percent_ID)+1)
	plt.title('Density plot of % identity of blast hits')
	plt.xlabel('Percentage of identity')
	plt.ylabel('Frequency')

	plt.savefig('percent_ID.png')




path_folder = sys.argv[1] # ./data/blast
list_files = sys.argv[2] # list_files.txt 


percent_identity_frequency(path_folder, list_files)
