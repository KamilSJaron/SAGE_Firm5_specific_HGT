import os, sys
import pandas as pd
import numpy as np

import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt


# gene_family should be like 'Bumble_Honey_bees_proteins/Gene_family_1058_parsed.out'
def plot_tax_identity(path_folder, gene_family, hierarchichal_tax):

	os.chdir(path_folder)
	

	hierarchical_tax_f = pd.read_table(hierarchical_tax, header=None)
	hierarchical_tax_f.columns = ['Query_ID', 'Tax_Hierarchy', 'Tax_Dist']


	gene_fam_f = open(gene_family, 'r')

	query=[]
	percent_ID=[]
	tax_dist=[]

	for line_GF in gene_fam_f:
		lline_GF = line_GF.split()

		if '#' not in lline_GF:
			if lline_GF[1].split('|')[1] in list(hierarchical_tax_f['Query_ID']):		
				query.append(lline_GF[1].split('|')[1])
				percent_ID.append(line_GF.split('\t')[2])
				tax_dist.append(int(hierarchical_tax_f[hierarchical_tax_f['Query_ID'] == lline_GF[1].split('|')[1]]['Tax_Dist']))





	plt.plot(tax_dist, percent_ID, 'ro')
	plt.grid(True)
	plt.xlim(min(tax_dist)-1,max(tax_dist)+1)
	plt.title(gene_family.split('/')[1])
	plt.xlabel('Hierarchical taxonomy distance')
	plt.ylabel('Percentage of identity')

	plt.savefig('tax_dist_ID_' + gene_family.split('/')[1] + '.png')


path_folder = sys.argv[1]
gene_family = sys.argv[2]
hierarchical_tax = sys.argv[3]


plot_tax_identity(path_folder, gene_family, hierarchical_tax)


