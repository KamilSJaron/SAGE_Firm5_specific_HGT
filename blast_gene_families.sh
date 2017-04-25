#!/bin/bash


bsub <<< """
#BSUB -L /bin/bash
#BSUB -o blast_$(basename $1).out
#BSUB -e blast_$(basename $1).err
#BSUB -J blast_$(basename $1)
#BSUB -n 8
#BSUB -R "span[ptile=8]"
#BSUB -M 20000000
#BSUB –R "rusage[mem=20000]"
#BSUB -u virginie.ricci@unil.ch


# 1. query
# 2. output


module add Blast/ncbi-blast/2.3.0+;

blastp -db refseq -query $1 -out $2 -outfmt '7 std stitle salltitles' -num_threads 8

"""

