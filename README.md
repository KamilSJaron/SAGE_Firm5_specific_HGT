### Firm5 specific ancient HGT

Repo of Jo and Virginie (Ninet93 or Baboo19)! 


## overview
This README.txt comprises details about folders and files.


##########################
## SAGE_Firm5_specific_HGT
##########################
This folder is synchronized with our github repo : https://github.com/KamilSJaron/SAGE_Firm5_specific_HGT.git
This repo is public.

scripts folder contains all scripts we created for data analysis.
data folder contains all data we are using as input or output.
test folder contains all testing scripts.


In SAGE_Firm5_specific_HGT, There are bash scripts (.sh), which are used to 'bsub' different scripts which are stored in scripts folder.
Each bash script has exactly the same name as its corresponding script in scripts folder.


##########
## scripts
##########
This folder contains all scripts we created for data analysis.

subgroup_sort.py:
input: Genefamilies_all.txt
outputs: in data/sort_group:  Bumble_bees.txt, Honey_bees.txt, Bumble_Honey_bees.txt, Outgroup.txt
Each output contains gene families of its bee group if 80% of all strains are present.
It means that for each gene family 'line' of Genefamilies_all.txt, if at least 80% of all strains of a bee group are present, the 'line' is stored into its corresponding bee group output file.

proteinseqextract.py:
inputs: outputs of subgroup_sort.py in data/sort_group (Bumble_bees.txt, Honey_bees.txt, Bumble_Honey_bees.txt or Outgroup.txt), all_proteins.fasta (of mls_2016/blast folder) 
outputs: in data: folders of Bumble_bees, Honey_bees, Bumble_Honey_bees and Outgroup - each folder contains .fasta files of gene families - a file concerns one gene family and contains all reference_genome|protein_ID and their sequence in fasta format

# test subfolder
The script subgroup_sort_test.py checks if all the different gene families (present in Genefamilies_all.txt) are sorted in the different filies according to the subgroup_sort.py. The test script allows also to determine the number of gene families present in each considered subgroups.



#######
## data
#######
This folder contains all data we are using as input or output.

GeneFamilies.txt: input
format: 'Gene_family_1	F225|1578.157.peg.1085	F225|1578.157.peg.957 ...'
'Gene_family '\t' reference_genome|protein_ID '\t' reference_genome|protein_ID ...'
Each line corresponds to a Gene_family. For each Gene_family, there are reference_genome|protein_ID for each protein which takes part to the corresponding Gene_family group.

Genefamilies_all.txt : old input - no more used


# sort_group subfolder
Contain files (.txt) according to the subgroup_sort.py script. 
The different files have the same structure as GeneFamilies.txt and represent the considered subgroups: Bumble_bees, Honey_bees and Bumble_Honey_bees. There is also Outgroup. 

# Honey_bees_proteins subfolder
This folder contains outputs (.fasta) of proteinseqextract.py script. 
Each fasta file corresponds to one Gene_family. It comprises protein sequences of all orthologous genes of the Gene_family. 

# Bumble_bees_proteins subfolder
This folder contains outputs (.fasta) of proteinseqextract.py script. 
Each fasta file corresponds to one Gene_family. It comprises protein sequences of all orthologous genes of the Gene_family.

# Bumble_Honey_bees_proteins subfolder
This folder contains outputs (.fasta) of proteinseqextract.py script.
Each fasta file corresponds to one Gene_family. It comprises protein sequences of all orthologous genes of the Gene_family.



