# -*- coding: utf-8 -*-
"""
Created on Tue May  9 13:48:02 2017

@author: Claivaz&Ricci
"""



import os
from Bio import Entrez

bee_folder=os.listdir()

strain_list=[]
dict_strain_tax={}

for folder in bee_folder:
    bee_file=os.listdir(folder)
    for file in bee_file:
        for line in file:
            if '#' not in line:
                if line.split('\t')[1].split('|')[1] not in strain_list:
                    strain_list.append(line.split('\t')[1].split('|')[1])



for strain_ID in strain_list:
    handle = Entrez.efetch(db="protein", id=strain_ID, rettype="gb", retmode="text")
    write_switch=False
    for line_handle in handle.readlines():
        if write_switch==True:
            dict_strain_tax[strain_ID]=line_handle.replace('; ','\\')
            write_switch=False
        elif 'ORGANISM' in line_handle:
            write_switch=True



strain_tax=open('hierarchical_taxonomy.txt','w')
reference='WP_052726720' #Lactobacillus apis reference, from GeneFamily1458 in Honey_bees_proteins
handle = Entrez.efetch(db="protein", id=reference, rettype="gb", retmode="text")
write_switch=False
for line_handle in handle.readlines():
    if write_switch==True:
        strain_tax.write('Reference\t'+line_handle.replace('; ','\\')+'\n')
        write_switch=False
    elif 'ORGANISM' in line_handle:
        write_switch=True



for keys_ID in dict_strain_tax.keys():
    strain_tax.write(keys_ID+'\t'+dict_strain_tax[keys_ID]+'\n')
    
strain_tax.close()
