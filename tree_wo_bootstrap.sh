#!/bin/bash
"""
Created on Thu May 23 2017

@author: Claivaz & Ricci

SCRIPT 9

tree_wo_bootstrap.sh runs RAXML tool to infer phylogenetic trees (without bootstrapping) 
of all aligned protein sequences of every blast hits of selected Gene_family_*_parsed.out  
(in its bee folder in data/alignment_potential_HGT/). 

Inputs: Gene_family_*_parsed.multifasta in its corresponding folder of group of bees 
(data/alignment_potential_HGT/Bumble_bees_proteins/, 
data/alignment_potential_HGT/Honey_bees_proteins/, 
data/alignment_potential_HGT/Bumble_Honey_bees_proteins/)

Outputs: ML_wo_bootstrap_Gene_family_*_parsed.out in data/alignment_potential_HGT/

>> RAxML_bestTree.ML_wo_bootstrap_Gene_family_*_parsed can then be opened using 
FigTree tool (available at http://tree.bio.ed.ac.uk/software/figtree/)
"""

#BSUB -L /bin/bash
#BSUB -o tree_wo_bootstrap.out
#BSUB -e tree_wo_bootstrap.err
#BSUB -J tree_wo_bootstrap
#BSUB -n 24
#BSUB -R "span[ptile=24]"
#BSUB -M 10000000
#BSUB –R "rusage[mem=10000]"
#BSUB -u virginie.ricci@unil.ch

module add Phylogeny/raxml/8.2.9;


cd /scratch/beegfs/monthly/mls_2016/claivaz_ricci/SAGE_Firm5_specific_HGT/data/alignment_potential_HGT/

for dir_file in $(cat ../parsed_blast/list_files.txt); do
	
	INPUT=${dir_file%.out}.multifasta
	OUTPUT=ML_wo_bootstrap_$(basename ${dir_file%.out})
	
	raxmlHPC -m PROTGAMMAGTR -p 12345 -s $INPUT -n $OUTPUT
done


# -m : substitutionModel - amino acid substitution model: GTR
# -p : Specify a random number seed for the parsimony inferences. This allows you to reproduce your results and will help me debug the program.
# -s : input
# -n : output
