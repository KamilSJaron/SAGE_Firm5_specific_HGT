#!/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 31 2017

@author: Claivaz & Ricci

SCRIPT 10


Two reference genomes from Bumble bees group (F5_237 and F5_245) and one from Honey bees group (Lb_183) are analysed. 
For each reference genome, we extract the protein name of every genes present in each Gene_family_* from 
GeneFamilies.txt (in data). Thanks to GeneBank files (mls_2016/genome_files), we recover the coordinates and 
the function of each protein. Then, we map the specific position of the protein onto its reference genome. 
These informations are printed in extract_coordinates_function_from_gbkfiles.out.
 
Input: GeneFamilies.txt in data, GeneBank files in mls_2016/genome_files

Outputs: *.png files , *.tsv files and MappingIntoGenome.txt in data/IslandViewerResults


python extract_coordinates_function_from_gbkfiles PATH/<ortho_table_file> PATH/<genebank_file> <genefamily_considered> <strain_considered>
python extract_coordinates_function_from_gbkfiles.py data/GeneFamilies.txt ../../genome_files/F5_237.gbk Gene_family_1058 F237
"""

### assigning different input arguments to variables 
import sys
ortho_table_file = str(sys.argv[1])
genebank_file = str(sys.argv[2])
genefamily_considered = str(sys.argv[3])
strain_considered = str(sys.argv[4])

ortho_table = open(ortho_table_file, 'r')

### extracting protein ID from the ortholog table
for ortho_table_line in ortho_table:
    if genefamily_considered in ortho_table_line:
        genefamily_data = ortho_table_line

protein_ID = genefamily_data.split(strain_considered)[1].replace('|', '').split('\t')[0]

### extracting gene coordinates and gene function (printed in extract_coordinates_function_from_gbkfiles.out)
genome_file = open(genebank_file, 'r')

right_cds = False
product_end = False
in_cds = False

for genome_file_line in genome_file:
        
    if right_cds and product_found and product_end == False:
        print(genefamily_considered + '\t' + strain_considered + '\t' + protein_ID 
              + '\t' + coordinates.replace('\t', '').replace('\n', '') + '\t' + 
              product.replace('\n', '').replace('\t', ''))
        break
    
    elif 'gene' in genome_file_line:
        in_cds = False
    elif product_end and '\\' not in genome_file_line:
        product = product + genome_file_line
        product_end = False
    elif 'CDS' in genome_file_line:
        in_cds = True
        product_found = False
        product_end = False
        coordinates = genome_file_line
    elif '|' + protein_ID + '"' in genome_file_line or '_' + protein_ID + '"' in genome_file_line:
        if in_cds:
            right_cds = True
    elif 'product' in genome_file_line:
        product = genome_file_line
        product_found = True
        if len(genome_file_line.split('"')) != 3:
            product_end = True
        