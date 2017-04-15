#!/bin/python3

from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
import os

def extractprotseq(bee_group, bee_folder, all_proteins_faa):
	bee_group_f=open(bee_group, 'r')
	all_prot_f=open(all_proteins_faa, 'r')

	os.chdir(bee_folder)

	genome_protseq={} #dico of each ref_genome|protein_ID and its amino acid sequence
	for seq_record in SeqIO.parse(all_prot_f, 'fasta'):
		genome_protseq[seq_record.id]=seq_record.seq


	for line in bee_group_f:
		lline=line.split()

		sequences=[] #list of ref_genome|protein_ID and its amino acid sequence of a Gene_family
		Gene_family=''		
		Gene_family=lline[0]
		prot_seq_fn=Gene_family + '.fasta' #output names
		

		lline_wo_0 =lline[1::] #line without first element = Gene_family_*

		for obj in lline_wo_0:
			if obj in genome_protseq.keys():
				record=SeqRecord(genome_protseq[obj], id=obj)
				sequences.append(record)
			else:
				print('obj not found in all_prot_f', obj)
		SeqIO.write(sequences, prot_seq_fn, 'fasta')


