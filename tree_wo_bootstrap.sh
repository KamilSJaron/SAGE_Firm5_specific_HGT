#!/bin/bash
"""
Created on Thu May 23 2017

@author: Claivaz & Ricci

SCRIPT 9

tree_wo_bootstrap.sh runs RAXML tool to infer phylogenetic trees (without bootstrapping) 
of all aligned protein sequences of every blast hits of selected Gene_family_*_parsed.out  
(in its bee folder in data/phylogeny_potential_HGT/). 

Inputs: Gene_family_*_parsed.multifasta in its corresponding folder of group of bees 
(data/phylogeny_potential_HGT/Bumble_bees_proteins/, 
data/phylogeny_potential_HGT/Honey_bees_proteins/, 
data/phylogeny_potential_HGT/Bumble_Honey_bees_proteins/) listed in 
list_files_HGT_to_trees.txt (data/parsed_blast)

Outputs: ML_wo_bootstrap_Gene_family_*_parsed.out in data/phylogeny_potential_HGT/RAxML_results/

>> RAxML_bestTree.ML_wo_bootstrap_Gene_family_*_parsed can then be opened using 
FigTree tool (available at http://tree.bio.ed.ac.uk/software/figtree/)
"""

#BSUB -L /bin/bash
#BSUB -o tree_wo_bootstrap.out
#BSUB -e tree_wo_bootstrap.err
#BSUB -J tree_wo_bootstrap
#BSUB -n 18
#BSUB -R "span[ptile=18]"
#BSUB -M 10000000
#BSUB –R "rusage[mem=10000]"
#BSUB -u virginie.ricci@unil.ch
#BSUB -q dee-long

module add Phylogeny/raxml/8.2.9;


cd /scratch/beegfs/monthly/mls_2016/claivaz_ricci/SAGE_Firm5_specific_HGT/data/phylogeny_potential_HGT/

mkdir -p RAxML_results

raxmlHPC -m PROTGAMMAAUTO -p 12345 -s Bumble_Honey_bees_proteins/Gene_family_1058_parsed.multifasta -n ML_wo_bootstrap_Gene_family_1058_parsed.out

raxmlHPC -m PROTGAMMAAUTO -p 12345 -s Bumble_Honey_bees_proteins/Gene_family_991_parsed.multifasta -n ML_wo_bootstrap_Gene_family_991_parsed.out

raxmlHPC -m PROTGAMMAAUTO -p 12345 -s Bumble_Honey_bees_proteins/Gene_family_1099_parsed.multifasta -n ML_wo_bootstrap_Gene_family_1099_parsed.out

raxmlHPC -m PROTGAMMAAUTO -p 12345 -s Bumble_Honey_bees_proteins/Gene_family_1048_parsed.multifasta -n ML_wo_bootstrap_Gene_family_1048_parsed.out

raxmlHPC -m PROTGAMMAAUTO -p 12345 -s Bumble_bees_proteins/Gene_family_1674_parsed.multifasta -n ML_wo_bootstrap_Gene_family_1674_parsed.out

raxmlHPC -m PROTGAMMAAUTO -p 12345 -s Bumble_bees_proteins/Gene_family_1675_parsed.multifasta -n ML_wo_bootstrap_Gene_family_1675_parsed.out

raxmlHPC -m PROTGAMMAAUTO -p 12345 -s Bumble_bees_proteins/Gene_family_1678_parsed.multifasta -n ML_wo_bootstrap_Gene_family_1678_parsed.out

raxmlHPC -m PROTGAMMAAUTO -p 12345 -s Bumble_bees_proteins/Gene_family_1757_parsed.multifasta -n ML_wo_bootstrap_Gene_family_1757_parsed.out


mv RAxML_* RAxML_results/

# -m : substitutionModel - amino acid substitution model: AUTO will test prot substitution models with and without empirical base frequencies
# -p : Specify a random number seed for the parsimony inferences. This allows you to reproduce your results and will help me debug the program.
# -s : input
# -n : output
