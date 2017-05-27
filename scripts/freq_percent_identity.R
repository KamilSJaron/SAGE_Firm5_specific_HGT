#!/usr/bin/Rscript

# module add R/3.3.2

setwd('/scratch/beegfs/monthly/mls_2016/claivaz_ricci/SAGE_Firm5_specific_HGT/data/blast')

bee_dir = list.dirs('./')

bumble_files = list.files(bee_dir[2])
honey_files = list.files(bee_dir[4])
bumble_honey_files = list.files(bee_dir[3])

bumble_perc_identity = c()
honey_perc_identity = c()
bumble_honey_perc_identity = c()

for (gene_fam in 1:length(bumble_files)){
	tmp_file = try(read.table(paste0(bee_dir[2], '/', bumble_files[gene_fam]), sep = '\t', header=TRUE), TRUE)
	if(class(tmp_file) != 'try-error'){

		bumble_perc_identity = tmp_file[,3]

	}
}

for (gene_fam in 1:length(honey_files)){
	tmp_file = try(read.table(paste0(bee_dir[4], '/', honey_files[gene_fam]), sep = '\t', header=TRUE), TRUE)
	if(class(tmp_file) != 'try-error'){

		honey_perc_identity = tmp_file[,3]
	}
}

for (gene_fam in 1:length(bumble_honey_files)){
	tmp_file = try(read.table(paste0(bee_dir[3], '/', bumble_honey_files[gene_fam]), sep = '\t', header=TRUE), TRUE)
	if(class(tmp_file) != 'try-error'){

		bumble_honey_perc_identity = tmp_file[,3]
	}
}

	
all_perc_identity = cbind(bumble_perc_identity, honey_perc_identity, bumble_honey_perc_identity)

Density = density(all_perc_identity)

pdf('Density_percent_identity_blast.pdf')
plot(Density)
dev.off()
