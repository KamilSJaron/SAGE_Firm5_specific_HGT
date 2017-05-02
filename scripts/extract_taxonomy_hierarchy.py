# -*- coding: utf-8 -*-
"""
Created on Tue May  2 18:45:19 2017

@author: Claivaz & Ricci

Script to extract the hierarchical classification of the hits' strain obtain from blast_hits_extract.py

remarque: maybe to insert those commands in blast_hits_extract.py
"""

#To delete | start                
import os
os.getcwd()
os.chdir('C:/Users/Claivaz/Desktop/Honey_bees_proteins')
parsed_file=open('Gene_family_1168_parsed.out','r')
#end 


from Bio import Entrez
Entrez.email = "joaquimclaivaz@gmail.com"     # Always tell NCBI who you are

parsed_file.readline()

for line_parsed in parsed_file:
    handle = Entrez.efetch(db="protein", id=line_parsed.split('\t')[1].split('|')[1], rettype="gb", retmode="text")
    write_switch=False
    for line_handle in handle.readlines():
        if write_switch==True:
            print(line_handle.replace('; ','\\'))
            write_switch=False
        elif 'ORGANISM' in line_handle:
            write_switch=True
            
#to delete / start
parsed_file.close()    
#end