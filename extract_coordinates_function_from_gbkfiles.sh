#!/bin/bash

#BSUB -L /bin/bash
#BSUB -o extract_coordinates_function_from_gbkfiles.out
#BSUB -e extract_coordinates_function_from_gbkfiles.err
#BSUB -J extract_coordinates_function_from_gbkfiles
#BSUB -n 8
#BSUB -R "span[ptile=8]"
#BSUB -M 10000000
#BSUB –R "rusage[mem=10000]"
#BSUB -u virginie.ricci@unil.ch



# GF: Gene_family_* (line) of GeneFamilies.txt file
# G_file: *.gbk (genome file)
# G_name: genome name



# BH: Bumble_Honey_bees
for GF_BH in 1058 991 1099 1086 1078 55 896 1072 1097 1059 1083; do

	for G_file_BH in F5_237.gbk F5_245.gbk Lb183.gbk; do

			if [ $G_file_BH = F5_237.gbk ]
			then
				INPUT_G_file=../../genome_files/$G_file_BH
				INPUT_G_name=F237
				INPUT_GF=Gene_family_$GF_BH

			elif [ $G_file_BH = F5_245.gbk ]
			then
				INPUT_G_file=../../genome_files/$G_file_BH
				INPUT_G_name=F245
				INPUT_GF=Gene_family_$GF_BH

			elif [ $G_file_BH = Lb183.gbk ]
			then
				INPUT_G_file=../../genome_files/$G_file_BH
				INPUT_G_name=L183
				INPUT_GF=Gene_family_$GF_BH

			fi
			python3 ./scripts/extract_coordinates_function_from_gbkfiles.py ./data/GeneFamilies.txt $INPUT_G_file $INPUT_GF $INPUT_G_name 
	done
done



# B: Bumble_bees
for GF_B in 1674 1675 1757 1678; do

	for G_file_B in F5_237.gbk F5_245.gbk; do

			if [ $G_file_B = F5_237.gbk ]
			then
				INPUT_G_file=../../genome_files/$G_file_B
				INPUT_G_name=F237
				INPUT_GF=Gene_family_$GF_BH

			elif [ $G_file_B = F5_245.gbk ]
			then
				INPUT_G_file=../../genome_files/$G_file_B
				INPUT_G_name=F245
				INPUT_GF=Gene_family_$GF_BH

			fi
			python3 ./scripts/extract_coordinates_function_from_gbkfiles.py ./data/GeneFamilies.txt $INPUT_G_file $INPUT_GF $INPUT_G_name 
	done
done