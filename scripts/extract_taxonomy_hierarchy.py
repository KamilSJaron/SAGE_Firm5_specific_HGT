# -*- coding: utf-8 -*-
"""
Created on Tue May  9 13:48:02 2017

@author: Claivaz&Ricci
"""

import os
from Bio import Entrez


Entrez.email = "virginie.ricci@unil.ch"


os.chdir('data/parsed_blast/')

bee_folder=os.listdir() #list: Bumble_bees_proteins, Honey_bees_proteins, Bumble_Honey_bees_proteins

strain_list=[]
dict_strain_tax={} # strain as keys and hierarchical taxonomy as items

for folder in bee_folder:
    bee_file=os.listdir(folder) #list each files in the folder
    for file in bee_file:
        file_read=open(folder+'/'+file,'r')
        for line in file_read:
            if '#' not in line:
                if line.split('\t')[1].split('|')[1] not in strain_list:
                    strain_list.append(line.split('\t')[1].split('|')[1]) #WP_****
        file_read.close()


for strain_ID in strain_list: #WP_****
    handle = Entrez.efetch(db="protein", id=strain_ID, rettype="gb", retmode="text")
    write_switch=False
    line_tmp=''
    for line_handle in handle.readlines():
        if write_switch==True and '.' in line_handle:
            line_tmp=line_tmp+line_handle
            line_tmp=line_tmp.replace(' ','').replace('\n','').replace('\t','').replace('.','')
            dict_strain_tax[strain_ID]=line_tmp
            write_switch=False
        elif write_switch==True:
            line_tmp=line_tmp+line_handle
        elif 'ORGANISM' in line_handle:
            write_switch=True



strain_tax=open('hierarchical_taxonomy.txt','w')
reference='WP_052726720' #Lactobacillus apis reference, from GeneFamily1458 in Honey_bees_proteins
handle = Entrez.efetch(db="protein", id=reference, rettype="gb", retmode="text")
write_switch=False
line_tmp=''
for line_handle in handle.readlines():
    if write_switch==True and '.' in line_handle:
        line_tmp=line_tmp+line_handle
        line_tmp=line_tmp.replace(' ','').replace('\n','').replace('\t','').replace('.','')
        ref_tax=line_tmp.split(';') #'Bacteria;Firmicutes;Bacilli;Lactobacillales;Lactobacillaceae;Lactobacillus'
        write_switch=False
        break
    elif write_switch==True:
        line_tmp=line_tmp+line_handle
    elif 'ORGANISM' in line_handle:
        write_switch=True


dict_distance={} # strain as keys and taxonomy distance as items
# more it is 'recent', smaller is the distance value

for keys_ID in dict_strain_tax.keys():
    taxo_tmp=dict_strain_tax[keys_ID]
    if ref_tax[5] in taxo_tmp:  #Lactobacillus
        dict_distance[keys_ID]=1
    elif ref_tax[4] in taxo_tmp: #Lactobacillaceae
        dict_distance[keys_ID]=2
    elif ref_tax[3] in taxo_tmp: #Lactobacillales
        dict_distance[keys_ID]=3
    elif ref_tax[2] in taxo_tmp: #Bacilli
        dict_distance[keys_ID]=4
    elif ref_tax[1] in taxo_tmp: #Firmicutes
        dict_distance[keys_ID]=5
    elif ref_tax[0] in taxo_tmp: #Bacteria
        dict_distance[keys_ID]=6
    else: #Not found
        dict_distance[keys_ID]=7
    
    strain_tax.write(keys_ID+'\t'+dict_strain_tax[keys_ID]+'\t'+str(dict_distance[keys_ID])+'\n')
    
strain_tax.close()
