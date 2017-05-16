#!/bin/bash

for dir in Bumble_bees_proteins Bumble_Honey_bees_proteins Honey_bees_proteins; do

	for file in $(cat ./data/$dir/list_files.txt); do
		mkdir -p data/blast/$dir
		bash blast_gene_families.sh ./data/$dir/$file ./data/blast/$dir/$(basename $file .fasta).out
	done

done


