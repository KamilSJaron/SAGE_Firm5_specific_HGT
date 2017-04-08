# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 18:28:06 2017

@author: Claivaz & Ricci

Script which select different genes specific to a given subgroup of firm-5 and write its specific file
Subgroup considered:Bombus sp. & Apis sp. & Apis/Bombus sp. &  Apis/Bombus/Out_lacto sp.
"""

import os
os.getcwd()
os.chdir('D:\\Unil\Master\Semester 2\SAGE\project')

###set different possible species
ortho_tab = open("Genefamilies_all.txt",'r')
ortho_tab.readline()

species_list=[]
for line in ortho_tab:
    species=line.split("\t")
    for spec in species:
        tmp_spec=spec.split("|")[0]
        if tmp_spec not in species_list and tmp_spec.split("_")[0]!="Gene":
            species_list.append(tmp_spec)

set(species_list)

#####create different subgroup
#'JF72':Lactobacillus apis ,'JF73':Lactobacillus helsingborgensis,'JF74':Lactobacillus melliventris,'JF75':Lactobacillus kimbladii,'JF76':Lactobacillus kullabergensis,'JG29':Lactobacillus mellis,'JG30':Lactobacillus mellifer,'L183':L. helsingborgensis,'L184':L melliventris, 'L185': L apis, 'L186': L Kullabergensis, 'LA14': Lactobacillus acidophilus (mammalian commensale/yoghurt), 'LA2':Lactobacillus amylovorus (pig) , 'LDB': L. delbrueckii (yoghurt), 'LGAS':Lactobacillus gasseri (Prebiotic/probiotic), 'LHV': Lactobacillus helveticus (cheese process),'LJP': Lactobacillus johnsonii (probiot/prebiot), 'WANG': L kefiranofaciens (pro/prebiot/kefir)
B_pascuorum=['F225','F230', 'F233', 'F234','F236','F237']
B_bohemicus=['F228', 'F245','F246','F247']
A_melifera=['F259','F260','F261','F262','F263']
Out_lacto=['JF72','JF73','JF74','JF75','JF76','JG29','JG30','L183','L184', 'L185', 'L186']
Outgroup=['LA14', 'LA2', 'LDB', 'LGAS', 'LHV','LJP', 'WANG']
#####loop writing the correct set/subgroup
ortho_tab = open("Genefamilies_all.txt",'r')
set1=open("set1.txt",'w') #Bumble set
set2=open("set2.txt","w") #Apis set
set3=open("set3.txt","w") #Bumble and Apis set
set4=open("set4.txt","w") #Bumble,Apis and Out_lacto set

for line in ortho_tab:
    b_b=False #Bumble bohemicus
    b_p=False #Bumble pascuorum
    a_m=False #Apis melifera
    o_l=False #outgroup lactobacillus sp. from honey gut
    o_g=False
    Lb185=False
    tmp=line.split("\t")
    for tmp_seq in tmp:
        seqtmp=tmp_seq.split("|")[0]
        if seqtmp in Outgroup:
            o_g=True
            break
        elif seqtmp in B_pascuorum:
            b_p=True
        elif seqtmp in B_bohemicus:
            b_b=True
        elif seqtmp in A_melifera:
            a_m=True
        elif seqtmp=='L185': #because only considerate this strain fro the Lactobacillus group !=yoghurt
            Lb185=True
            o_l=True
        elif seqtmp in Out_lacto: 
            o_l=True
    if not o_g:
        if b_b and b_p:
            if not a_m and not o_l:
                set1.write(line)
            elif a_m and not o_l:
                set3.write(line)
            elif Lb185:
                set4.write(line)
        elif a_m and not o_l and not b_b and not b_p:
            set2.write(line)
            
set1.close()    
set2.close()
set3.close()
set4.close()
ortho_tab.close()
