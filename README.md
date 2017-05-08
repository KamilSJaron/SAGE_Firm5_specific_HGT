## SAGE_Firm5_specific_HGT

This folder is synchronized with our github repo : https://github.com/KamilSJaron/SAGE_Firm5_specific_HGT.git
This repo is public.

scripts folder contains all scripts we created for data analysis.
data folder contains all data we are using as input or output.
test folder contains all testing scripts.


In `SAGE_Firm5_specific_HGT`, There are bash scripts (`.sh`), which are used to `bsub` different scripts which are stored in scripts folder.
Each bash script has exactly the same name as its corresponding script in scripts folder.


### scripts

This folder contains all scripts we created for data analysis.

`subgroup_sort.py`:
- input: `Genefamilies_all.txt`
- outputs: in `data/sort_group`:  `Bumble_bees.txt`, `Honey_bees.txt`, `Bumble_Honey_bees.txt`, `Outgroup.txt`
- Each output contains gene families of its bee group if 80% of all strains are present.
- It means that for each gene family 'line' of `Genefamilies_all.txt`, if at least 80% of all strains of a bee group are present, the 'line' is stored into its corresponding bee group output file.

`proteinseqextract.py`:
- inputs: outputs of `subgroup_sort.py` in `data/sort_group` (`Bumble_bees.txt`, `Honey_bees.txt`, `Bumble_Honey_bees.txt` or `Outgroup.txt`), `all_proteins.fasta` (of `mls_2016/blast` folder)
- outputs: in `data`: folders of Bumble_bees_proteins, Honey_bees_proteins, Bumble_Honey_bees_proteins
- Each folder contains `.fasta` files of gene families - a file concerns one gene family and contains all reference_genome|protein_ID and their sequence in fasta format.

`blast_gene_families.sh`:
- Generalized function to perform blastp
- This function is associated with `function_blast.sh`
- Blastp will search for matches in RefSeq database.
- outputs will contain 14 columns: query id, subject id, % identity, alignment length, mismatches, gap opens, q. start, q. end, s. start, s. end, evalue, bit score, subject title, subject titles

`function_blast.sh`:
- inputs: outputs of `proteinseqextract.py`in `data` subfolders (Bumble_bees_proteins, Bumble_Honey_bees_proteins, Honey_bees_proteins) - each `.fasta` file corresponds to a gene family and contains all orthologous reference_genome|protein_ID and their sequence
- outputs: in  `data/blast`: folders of Bumble_bees_proteins, Honey_bees_proteins and Bumble_Honey_bees_proteins
- Each folder contains resulting blast files (`.out` format) - each file concerns blast results for every sequences of their corresponding gene family.

`blast_hits_extract.py`:
- inputs: outputs of `blast_gene_families.sh` in `data/blast` subfolders and different thresholds for trimming the different hits - each `.out` file corresponds to a gene family and contains the hits from `blast_gene_families.sh`.
- outputs will contain the different hits according to the thresholds (and excluding hits from Lactobacillus sp.). The structure of the `_parsed.out` files is columns with Query_ID, Subject_titles, %_Identity, Alignment_length, evalue, bit_score

`blast_hits_extract.sh`:
- script to run `blast_hits_extract.py` on every files present in `data/blast` folders (Bumble_bees_proteins, Bumble_Honey_bees_proteins, Honey_bees_proteins)

`extract_taxonomy_hierarchy.py`:
- inputs: outputs of `blast_hits_extract.py`
- outputs: TO CHANGE, print the hierarchical taxonomy. Maybe to consider the integration of this script in the function `blast_hits_extract.py'.
- extraction of classifical hierarchy of the strain from genebank


### test subfolder

The script `subgroup_sort_test.py` checks if all the different gene families (present in `Genefamilies_all.txt`) are sorted in the different filies according to the `subgroup_sort.py`. The test script allows also to determine the number of gene families present in each considered subgroups.


### data

This folder contains all data we are using as input or output.

`GeneFamilies.txt`: input
- format:

```
Gene_family_1	F225|1578.157.peg.1085	F225|1578.157.peg.957 ...
'Gene_family '\t' reference_genome|protein_ID '\t' reference_genome|protein_ID ...
```

- Each line corresponds to a Gene_family. For each Gene_family, there are reference_genome|protein_ID for each protein which takes part to the corresponding Gene_family group.

`Genefamilies_all.txt` : old input - no more used


### sort_group subfolder

This folder contain files (`.txt`) according to the `subgroup_sort.py` script.
The different files have the same structure as GeneFamilies.txt and represent the considered subgroups: Bumble_bees, Honey_bees and Bumble_Honey_bees. There is also Outgroup.


### Honey_bees_proteins subfolder

This folder contains outputs (`.fasta`) of `proteinseqextract.py` script.
Each fasta file corresponds to one Gene_family. It comprises protein sequences of all orthologous genes of the Gene_family.


### Bumble_bees_proteins subfolder

This folder contains outputs (`.fasta`) of `proteinseqextract.py` script.
Each fasta file corresponds to one Gene_family. It comprises protein sequences of all orthologous genes of the Gene_family.


### Bumble_Honey_bees_proteins subfolder

This folder contains outputs (`.fasta`) of `proteinseqextract.py` script.
Each fasta file corresponds to one Gene_family. It comprises protein sequences of all orthologous genes of the Gene_family.


### blast subfolder

This folder contains subfolders: Bumble_bees_proteins, Bumble_Honey_bees_proteins, Honey_bees_proteins
Each folder contains `.out` output files of `blast_gene_families.sh` and `function_blast.sh` scripts.
Each file corresponds to blast results of one Gene_family (blast on protein sequences of all orthologous genes). It contains 14 columns summarizing blast hits and the taxonomic name of the strain (columns: query id, subject id, % identity, alignment length, mismatches, gap opens, q. start, q. end, s. start, s. end, evalue, bit score, subject title, subject titles).
