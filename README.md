## SAGE_Firm5_specific_HGT

This folder is synchronized with our github repo : https://github.com/KamilSJaron/SAGE_Firm5_specific_HGT.git
This repo is public.

- scripts folder contains all scripts we created for data analysis.
- data folder contains all data we are using as input or output.
- test folder contains all testing scripts and testing results.


In `SAGE_Firm5_specific_HGT`, there are bash scripts (`.sh`), which are used to `bsub` different scripts which are stored in scripts folder.
Each bash script has exactly the same name as its corresponding script in scripts folder.


### scripts

This folder contains all scripts (`.py` and `.R`) we created for data analysis.

`subgroup_sort.py` (1):
- input: `Genefamilies_all.txt`
- outputs: in `data/sort_group`:  `Bumble_bees.txt`, `Honey_bees.txt`, `Bumble_Honey_bees.txt`, `Outgroup.txt`
- Each output file contains gene families of its bee group if 80% of all strains are present.
- It means that for each gene family 'line' of `Genefamilies_all.txt`, if at least 80% of all strains of a bee group are present, the 'line' is stored into its corresponding bee group output file.


`proteinseqextract.py` (2):
- inputs: outputs of `subgroup_sort.py` in `data/sort_group` (`Bumble_bees.txt`, `Honey_bees.txt`, `Bumble_Honey_bees.txt` or `Outgroup.txt`), `all_proteins.fasta` (of `mls_2016/blast` folder)
- outputs: in `data`: folders of Bumble_bees_proteins, Honey_bees_proteins, Bumble_Honey_bees_proteins
- Each output folder contains `.fasta` files of gene families - a file concerns one gene family and contains all reference_genome|protein_ID and their sequence in fasta format.


`blast_hits_extract.py` (4):
- inputs: outputs of `blast_gene_families.sh` in `data/blast` subfolders (Bumble_bees_proteins, Honey_bees_proteins and Bumble_Honey_bees_proteins)
- outputs: in  `data/parsed_blast`: folders of Bumble_bees_proteins, Honey_bees_proteins and Bumble_Honey_bees_proteins
- Each output folder contains parsed resulting blast files (`_parsed.out` format) - each file concerns parsed blast results for every sequences of their corresponding gene family.
- The header of each `_parsed.out` files is: Query_ID, Subject_titles, %_Identity, Alignment_length, evalue, bit_score


`extract_taxonomy_hierarchy.py` (5):
- inputs: outputs of `blast_hits_extract.py` in `data/parsed_blast` subfolders (Bumble_bees_proteins, Honey_bees_proteins and Bumble_Honey_bees_proteins)
- outputs: in  `data/parsed_blast`: `hierarchical_taxonomy.txt`: list of strain IDs and their corresponding hierarchical taxonomy and subjective hierarchical taxonomy distance (as followed)
- Lactobacillus = 1
- Lactobacillaceae = 2
- Lactobacillales = 3
- Bacilli = 4
- Firmicutes = 5
- Bacteria = 6
- None = 7 (which either corresponds to Archae or Eukaryota - contaminations)


`plot_identity_taxonomy.R` (6):
- inputs: in  `data/parsed_blast`: outputs of `blast_hits_extract.py` and `hierarchical_taxonomy.txt`
- outputs: in `data/parsed_blast`: Bumble_taxo_plot.pdf, Honey_taxo_plot.pdf and Bumble_Honey_taxo_plot.pdf in addition to potential_HGT.txt
- Each `.pdf` file contains all plots (percentage of identity between query and subject against hierachical taxonomy distance) of a bee group. 
- potential_HGT.txt lists all files of gene family that contains orthologous genes that are potentially acquired by HGT. 

`extract_seq_blast_hits.py` (7):
- inputs:
- outputs:




### SAGE_Firm5_specific_HGT

This folder contains all scripts (`.sh`) we created for data analysis - does not comprise bash scripts (`.sh`) which are used to `bsub` other scripts.

`blast_gene_families.sh` (3.1):
- Generalized function to perform blastp
- This function is associated with `function_blast.sh`
- Blastp will search for matches in RefSeq database.
- Each output contains 14 columns: query id, subject id, % identity, alignment length, mismatches, gap opens, q. start, q. end, s. start, s. end, evalue, bit score, subject title, subject titles

`function_blast.sh` (3.2):
- inputs: outputs of `proteinseqextract.py`in `data` subfolders (Bumble_bees_proteins, Bumble_Honey_bees_proteins, Honey_bees_proteins) - each `.fasta` file corresponds to a gene family and contains all orthologous reference_genome|protein_ID and their sequence
- outputs: in  `data/blast`: folders of Bumble_bees_proteins, Honey_bees_proteins and Bumble_Honey_bees_proteins
- Each output folder contains resulting blast files (`.out` format) - each file concerns blast results for every sequences of their corresponding gene family.

`align_potential_HGT.sh` (8):
- inputs:
- outputs:

`tree_wo_bootstrap.sh` (9):
- inputs:
- outputs: 

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


### parsed_blast subfolder

This folder contains subfolders: Bumble_bees_proteins, Bumble_Honey_bees_proteins, Honey_bees_proteins
Each folder contains `_parsed.out` output files of `blast_hits_extract.py` and `blast_hits_extract.sh` scripts.
Each file corresponds to parsed blast results of one Gene_family (blast on protein sequences of all orthologous genes). It contains 6 columns summarizing blast hits and the taxonomic name of the strain (columns: Query_ID, Subject_titles, %_Identity, Alignment_length, evalue, bit_score).
