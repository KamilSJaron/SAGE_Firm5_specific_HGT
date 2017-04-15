# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 18:28:06 2017

@author: Claivaz & Ricci

Script which select different genes specific to a given subgroup of firm-5 and write its specific file
Subgroup considered:Bombus sp. & Apis sp. & Apis/Bombus sp.
"""

#####create different subgroup
#'JF72':Lactobacillus apis ,'JF73':Lactobacillus helsingborgensis,'JF74':Lactobacillus melliventris,'JF75':Lactobacillus kimbladii,'JF76':Lactobacillus kullabergensis,'JG29':Lactobacillus mellis,'JG30':Lactobacillus mellifer,'L183':L. helsingborgensis,'L184':L melliventris, 'L185': L apis, 'L186': L Kullabergensis, 'LA14': Lactobacillus acidophilus (mammalian commensale/yoghurt), 'LA2':Lactobacillus amylovorus (pig) , 'LDB': L. delbrueckii (yoghurt), 'LGAS':Lactobacillus gasseri (Prebiotic/probiotic), 'LHV': Lactobacillus helveticus (cheese process),'LJP': Lactobacillus johnsonii (probiot/prebiot), 'WANG': L kefiranofaciens (pro/prebiot/kefir)
B_pascuorum=['F225','F230','F233','F234','F236','F237']
B_bohemicus=['F228', 'F245','F246','F247']
Bumble=B_pascuorum+B_bohemicus
A_mellifera=['JF72','JF73','JG30','JF74','JF75','JF76','F259','F260','F261','F262','F263','L183','L184','L185','L186']
Honey=A_mellifera
Outgroup=['JG29','LA14','LA2','LDB','LGAS','LHV','LJP','WANG']
#####loop writing the correct set/subgroup
Ortho_tab=open("data/GeneFamilies.txt",'r')
Bumble_bees_f=open("data/sort_group/Bumble_bees.txt",'w') #Bumble set
Honey_bees_f=open("data/sort_group/Honey_bees.txt","w") #Apis set
Bumble_Honey_bees_f=open("data/sort_group/Bumble_Honey_bees.txt","w") #Bumble and Apis set
Outgroup_f=open("data/sort_group/Outgroup.txt","w")

def are_all_in_line(group_bee,line,threshold):
    threshold_limit=1
    one_strain_present=False
    for strain in group_bee:
        if strain not in line:
            threshold_limit-=1/len(group_bee)
            if threshold_limit < threshold and one_strain_present:
                return 'Partial'
        else:
            one_strain_present=True
    if threshold_limit > threshold:
        return True
    elif one_strain_present:
        return 'Partial'
    else:
        return False

threshold=0.8
###
for line in Ortho_tab:
    Bumble_tmp=are_all_in_line(Bumble,line,threshold)
    Honey_tmp=are_all_in_line(Honey,line,threshold)
    Outgroup_tmp=are_all_in_line(Outgroup,line,threshold)
    if not Outgroup_tmp:
        if Bumble_tmp==True:
            if Honey_tmp==True:
                Bumble_Honey_bees_f.write(line)
            elif not Honey_tmp:
                Bumble_bees_f.write(line)
            else:
                Outgroup_f.write(line)
        elif not Bumble_tmp and Honey_tmp==True:
            Honey_bees_f.write(line)
        else:
            Outgroup_f.write(line)
    else:
        Outgroup_f.write(line)



Bumble_bees_f.close()    
Honey_bees_f.close()
Bumble_Honey_bees_f.close()
Outgroup_f.close()
Ortho_tab.close()
