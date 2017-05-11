import os
import pandas as pd
import numpy as np

import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt



os.chdir('data/parsed_blast')


hierarchical_tax_fn = 'hierarchical_taxonomy.txt'
#hierarchical_tax_f = open(hierarchical_tax_fn, 'r')

hierarchical_tax_f = pd.read_table(hierarchical_tax_fn, header=None)
hierarchical_tax_f.columns = ['Query_ID', 'Tax_Hierarchy', 'Tax_Dist']


gene_fam_fn = 'Bumble_Honey_bees_proteins/Gene_family_1058_parsed.out'
gene_fam_f = open(gene_fam_fn, 'r')



query=[]
percent_ID=[]
tax_dist=[]

for line_GF in gene_fam_f:
		lline_GF = line_GF.split()

		if '#' not in lline_GF:
				if lline_GF[1].split('|')[1] in list(hierarchical_tax_f['Query_ID']):	
#					print(hierarchical_tax_f[hierarchical_tax_f['Query_ID'] == lline_GF[1].split('|')[1]])
#					print(lline_GF[1].split('|')[1], line_GF.split('\t')[2], int(hierarchical_tax_f[hierarchical_tax_f['Query_ID'] == lline_GF[1].split('|')[1]]['Tax_Dist']))
					
					query.append(lline_GF[1].split('|')[1])
					percent_ID.append(line_GF.split('\t')[2])
					tax_dist.append(int(hierarchical_tax_f[hierarchical_tax_f['Query_ID'] == lline_GF[1].split('|')[1]]['Tax_Dist']))





plt.plot(tax_dist, percent_ID, 'ro')
plt.grid(True)
plt.xlim(min(tax_dist)-1,max(tax_dist)+1)
plt.title(gene_fam_fn.split('/')[1])
plt.xlabel('Hierarchical taxonomy distance')
plt.ylabel('Percentage of identity')



#plt.show()
plt.savefig('tax_dist_ID' + gene_fam_fn + '.png')			



