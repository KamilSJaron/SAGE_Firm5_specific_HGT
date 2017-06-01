#!/usr/bin/Rscript
# -*- coding: utf-8 -*-
#
# Created on Tue May 17 2017
#
# @author: Claivaz & Ricci
#
# SCRIPT extra - cf. freq_precent_identity.R
#
# freq_precent_identity.R plots every percent identity values of every blast hits
# (density plot)

# Input: Percent_ID_list.txt in data/blast/
#
# Output: Density_percent_identity_blast.pdf data/blast/

# module add R/3.3.2

setwd('/scratch/beegfs/monthly/mls_2016/claivaz_ricci/SAGE_Firm5_specific_HGT')

Percent_ID_list <- read.table('Percent_ID_list.txt', header=FALSE)

Density = density(Percent_ID_list[,1])


setwd('/scratch/beegfs/monthly/mls_2016/claivaz_ricci/SAGE_Firm5_specific_HGT/data/blast')

pdf('Density_percent_identity_blast.pdf')
plot(Density, main='Density plot of all percent identity of every blast hits', xlab='% identity')
abline(v=50, col='red')
dev.off()
