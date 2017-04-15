### Firm5 specific HGT

Repo of Jo and Virginie (Ninet93 or Baboo19)! 


## overview
This README.txt comprises details about folders and files.


## SAGE_Firm5_specific_HGT
This folder is synchronized with our github repo : https://github.com/KamilSJaron/SAGE_Firm5_specific_HGT.git
This repo is public.

scripts folder contains all scripts we created for data analysis.
data folder contains all data we are using as input or output.
test folder contains all testing scripts.


In SAGE_Firm5_specific_HGT, There are bash scripts (.sh), which are used to 'bsub' different scripts which are stored in scripts folder.
Each bash script has exactly the same name as its corresponding script in scripts folder.



## scripts
This folder contains all scripts we created for data analysis.

subgroup_sort.py:
input: Genefamilies_all.txt
ouputs: Bumble_bees.txt, Honey_bees.txt, Bumble_Honey_bees.txt, Outgroup.txt
Each output contains gene families of its bee group if 80% of all strains are present.
It means that for each gene family 'line' of Genefamilies_all.txt, if at least 80% of all strains of a bee group are present, the 'line' is stored into its corresponding bee group output file.

proteinseqextract.py:
inputs: ouputs of subgroup_sort.py (Bumble_bees.txt, Honey_bees.txt, Bumble_Honey_bees.txt or Outgroup.txt), all_proteins.fasta (of mls_2016/blast folder) 
outputs: folder of Bumble_bees, Honey_bees, Bumble_Honey_bees and Outgroup - each folder contains .fasta files of gene families - a file concerns one gene family and contains all reference_genome|protein_ID and their sequence in fasta format



## data
This folder contains all data we are using as input or output.

Genefamilies_all.txt: input
format: 'Gene_family_1	F225|1578.157.peg.1085	F225|1578.157.peg.957 ...'
'Gene_family '\t' reference_genome|protein_ID '\t' reference_genome|protein_ID ...'
Each line corresponds to a Gene_family. For each Gene_family, there are reference_genome|protein_ID for each protein which takes part to the corresponding Gene_family group.



