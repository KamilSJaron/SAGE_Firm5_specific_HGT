# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 18:28:06 2017

@author: Claivaz & Ricci

Script which select different genes specific to a given subgroup of firm-5 and write its specific file
Subgroup considered:Bombus sp. & Apis sp. & Apis/Bombus sp. &  Apis/Bombus/Out_lacto sp.
"""

import os

###set different possible species
Ortho_tab = open("data/Genefamilies_all.txt",'r')
Ortho_tab.readline()

species_list=[]
for line in Ortho_tab:
    split_line_bytab=line.split("\t")
    for obj in split_line_bytab:
        species=obj.split("|")[0]
        if species not in species_list and species.split("_")[0]!="Gene":
            species_list.append(species)

print(set(species_list))

#####create different subgroup
#'JF72':Lactobacillus apis ,'JF73':Lactobacillus helsingborgensis,'JF74':Lactobacillus melliventris,'JF75':Lactobacillus kimbladii,'JF76':Lactobacillus kullabergensis,'JG29':Lactobacillus mellis,'JG30':Lactobacillus mellifer,'L183':L. helsingborgensis,'L184':L melliventris, 'L185': L apis, 'L186': L Kullabergensis, 'LA14': Lactobacillus acidophilus (mammalian commensale/yoghurt), 'LA2':Lactobacillus amylovorus (pig) , 'LDB': L. delbrueckii (yoghurt), 'LGAS':Lactobacillus gasseri (Prebiotic/probiotic), 'LHV': Lactobacillus helveticus (cheese process),'LJP': Lactobacillus johnsonii (probiot/prebiot), 'WANG': L kefiranofaciens (pro/prebiot/kefir)
B_pascuorum=['F225','F230','F233','F234','F236','F237']
B_bohemicus=['F228', 'F245','F246','F247']
A_melifera=['F259','F260','F261','F262','F263']
Outgroup_wo_yogurt=['JF72','JF73','JF74','JF75','JF76','JG29','JG30','L183','L184','L185','L186']
Outgroup_w_yogurt=['LA14','LA2','LDB','LGAS','LHV','LJP','WANG']
#####loop writing the correct set/subgroup
Ortho_tab=open("data/Genefamilies_all.txt",'r')
Bumble_bees_f=open("Bumble_bees.txt",'w') #Bumble set
Honey_bees_f=open("Honey_bees.txt","w") #Apis set
Bumble_Honey_bees_f=open("Bumble_Honey_bees.txt","w") #Bumble and Apis set
Bumble_Honey_Lacto_bees_f=open("Bumble_Honey_Lacto_bees.txt","w") #Bumble,Apis and Out_lacto set

for line in Ortho_tab:
    B_bohemicus_TF=False
    B_pascuorum_TF=False
    A_melifera_TF=False
    Outgroup_wo_yogurt_TF=False
    Outgroup_w_yogurtTF=False
    split_line_bytab=line.split("\t")
    for obj in split_line_bytab:
        strains=obj.split("|")[0]
        if strains in Outgroup:
            Outgroup_TF=True
            break
        elif strains in B_pascuorum:
            B_pascuorum_TF=True
        elif strains in B_bohemicus:
            B_bohemicus_TF=True
        elif strains in A_melifera:
            A_melifera_TF=True
        elif strains in Out_lacto:
            Out_lacto_TF=True
    if not Outgroup_TF:
        if B_bohemicus_TF and B_pascuorum_TF:
            if not A_melifera_TF and not Out_lacto_TF:
                Bumble_bees_f.write(line)
            elif A_melifera_TF and not Out_lacto_TF:
                Bumble_Honey_bees_f.write(line)
            else:
                Bumble_Honey_Lacto_bees_f.write(line)
        elif A_melifera_TF and not Out_lacto_TF and not B_bohemicus_TF and not B_pascuorum_TF:
            Honey_bees_f.write(line)
            
Bumble_bees_f.close()    
Honey_bees_f.close()
Bumble_Honey_bees_f.close()
Bumble_Honey_Lacto_bees_f.close()
Ortho_tab.close()
