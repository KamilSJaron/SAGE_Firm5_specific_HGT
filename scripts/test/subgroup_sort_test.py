# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 15:14:04 2017

@author: Claivaz & Ricci

Script which test whether all gene families are sorted in different files and allows to know how many gene families are present in each group.
"""
Ortho_tab = open("data/GeneFamilies.txt", 'r')
Bumble_bees_f = open("data/sort_group/Bumble_bees.txt", 'r') #Bumble set
Honey_bees_f = open("data/sort_group/Honey_bees.txt", "r") #Apis set
Bumble_Honey_bees_f = open("data/sort_group/Bumble_Honey_bees.txt", "r") #Bumble and Apis set
Outgroup_f = open("data/sort_group/Outgroup.txt", "r")

expected_gene_family = []
sort_gene_family = []

def check_function(file_to_check, list_append):
    for genefam in file_to_check:
        if genefam.split('\t')[0].split('_')[0] == 'Gene':
            list_append.append(genefam.split('\t')[0])
            
check_function(Ortho_tab, expected_gene_family)
check_function(Bumble_bees_f, sort_gene_family)
check_function(Honey_bees_f, sort_gene_family)
check_function(Bumble_Honey_bees_f, sort_gene_family)
check_function(Outgroup_f, sort_gene_family)

if sort_gene_family.sort() == expected_gene_family.sort():
    print('all the gene families were sorted')

sort_gene_family_bumble = []
sort_gene_family_honey = []
sort_gene_family_bumble_and_honey = []
Bumble_bees_f = open("data/sort_group/Bumble_bees.txt", 'r') #Bumble set
Honey_bees_f = open("data/sort_group/Honey_bees.txt", "r") #Apis set
Bumble_Honey_bees_f = open("data/sort_group/Bumble_Honey_bees.txt", "r") #Bumble and Apis set

check_function(Bumble_bees_f, sort_gene_family_bumble)
check_function(Honey_bees_f, sort_gene_family_honey)
check_function(Bumble_Honey_bees_f, sort_gene_family_bumble_and_honey)

print('there is %d, %d, %d gene families in bumble, honey and bumble/honey respectively subgroups'%(len(sort_gene_family_bumble),len(sort_gene_family_honey),len(sort_gene_family_bumble_and_honey)))

Bumble_bees_f.close()    
Honey_bees_f.close()
Bumble_Honey_bees_f.close()
Outgroup_f.close()
Ortho_tab.close()
     
