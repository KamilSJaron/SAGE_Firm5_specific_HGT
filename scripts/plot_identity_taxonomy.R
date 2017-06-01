#!/usr/bin/Rscript
# -*- coding: utf-8 -*-
#
# Created on Tue May 17 2017
#
# @author: Claivaz & Ricci
#
# SCRIPT 6
#
# For every parsed blast results of each reference_genome|protein_ID’s sequence (query) 
# present in each Gene_family_*_parsed.out files in each folder of group of bees 
# (data/parsed_blast/Bumble_bees_proteins/, data/parsed_blast/Honey_bees_proteins/, 
# data/parsed_blast/Bumble_Honey_bees_proteins/), plot_identity_taxonomy.R extracts its 
# percentage of identity and its hierarchical taxonomy distance (in hierarchical_taxonomy.txt) 
# and plot them against each other. Moreover, for each Gene_family_*_parsed.out, 
# on one hand, we will perform linear regression model in addition to polynomial model and 
# investigate if models differ. If they differ, it would mean that polynomial model is the 
# best one and suggest potential horizontal gene transfer (ANOVA). 

# Inputs: Gene_family_*_parsed.out of its corresponding folder of group of bees 
# (data/parsed_blast/Bumble_bees_proteins/, data/parsed_blast/Honey_bees_proteins/, 
# data/parsed_blast/Bumble_Honey_bees_proteins/) and hierarchical_taxonomy.txt in data/parsed_blast/
# 
# Outputs: Bumble_taxo_plot.pdf, Honey_taxo_plot.pdf, Bumble_Honey_taxo_plot.pdf and 
# potential_HGT.txt in data/parsed_blast/ - each *.pdf file contains all plots of a given 
# bee group - potential_HGT.txt contains a list of Gene_family_*_parsed.out that are 
# orthologous genes potentially acquired by HGT

# module add R/3.3.2


setwd('/scratch/beegfs/monthly/mls_2016/claivaz_ricci/SAGE_Firm5_specific_HGT/data/parsed_blast')

### loading hierarchical taxonomy and listing all out files from parsed blast
taxo_hierarchical = read.table('hierarchical_taxonomy.txt', sep = '\t')
bee_dir = list.dirs('./')
bumble_files = list.files(bee_dir[2])
honey_files = list.files(bee_dir[4])
bumble_honey_files = list.files(bee_dir[3])



i = 1
potential_HGT = c() # listing all potential HGT based on ANOVA test of linear and polynomial models

### Bumble specific plots
pdf('Bumble_taxo_plot.pdf')

for (gene_fam in 1:length(bumble_files)){
  tmp_file = try(read.table(paste0(bee_dir[2], '/', bumble_files[gene_fam]),sep = '\t'), TRUE)
  if(class(tmp_file) != 'try-error'){
    
    perc_identity = c()
    dist_taxo = c()
    
    for (specie in 1:dim(tmp_file)[1]){
      perc_identity[specie] = tmp_file[specie,3]
      dist_taxo[specie] = taxo_hierarchical$V3[taxo_hierarchical$V1 == strsplit(as.character(tmp_file[specie,2]),
                                                                                '|',fixed = T)[[1]][2]]
    }
    for_model = data.frame(xvals = dist_taxo, yvals = perc_identity)
    
    fit = lm(yvals ~ xvals + I(xvals^2), data = for_model)
    fit2 = lm(yvals ~ xvals, data = for_model)
    
    prd = data.frame(xvals = seq(from = 1, to = 10, length.out = 100))
    prd$predicted = predict(fit, newdata = prd)
    
    plot(for_model$xvals, for_model$yvals,main = paste0(strsplit(bee_dir[2], './/',fixed=T)[[1]][2], '\n',
                                                        strsplit(bumble_files[gene_fam],'_parsed')[[1]][1]),
                                                        ylab='similarity [%]', xlab='hierarchical taxonomy distance [-]', xlim=range(1:7))

#    if(class(try(abline(fit2),TRUE)) != 'try-error'){
#      lines(prd$xvals, prd$predicted)
#      abline(fit2)
#    }
    
    
    
    tmp_pvalue = anova(fit, fit2)$Pr[2]
    
    if(all(is.na(tmp_pvalue) != TRUE, tmp_pvalue<0.05)){
      potential_HGT[i] = paste0(strsplit(bee_dir[2], './/', fixed=T)[[1]][2], '/', bumble_files[gene_fam])
      i = i+1
    }
  }
}

dev.off()



### Honey specific plots
pdf('Honey_taxo_plot.pdf')

for (gene_fam in 1:length(honey_files)){
  tmp_file = try(read.table(paste0(bee_dir[4], '/', honey_files[gene_fam]), sep = '\t'), TRUE)
  if(class(tmp_file) != 'try-error'){
    
    perc_identity = c()
    dist_taxo = c()
    
    for (specie in 1:dim(tmp_file)[1]){
      perc_identity[specie] = tmp_file[specie,3]
      dist_taxo[specie] = taxo_hierarchical$V3[taxo_hierarchical$V1 == strsplit(as.character(tmp_file[specie,2]),
                                                                                '|',fixed = T)[[1]][2]]
    }
    for_model = data.frame(xvals = dist_taxo, yvals = perc_identity)
    
    fit = lm(yvals ~ xvals + I(xvals^2), data = for_model)
    fit2 = lm(yvals ~ xvals, data = for_model)
    
    prd = data.frame(xvals = seq(from = 1, to = 10, length.out = 100))
    prd$predicted = predict(fit, newdata = prd)
    
    plot(for_model$xvals, for_model$yvals,main = paste0(strsplit(bee_dir[4],'.//',fixed = T)[[1]][2],
                                                        '\n',strsplit(honey_files[gene_fam],'_parsed')[[1]][1]),
                                                        ylab = 'similarity [%]', xlab = 'hierarchical taxonomy distance [-]', xlim=range(1:7))

#    if(class(try(abline(fit2),TRUE)) != 'try-error'){
#      lines(prd$xvals, prd$predicted)
#      abline(fit2)
#    }
    
    tmp_pvalue = anova(fit, fit2)$Pr[2]
    
    if(all(is.na(tmp_pvalue) != TRUE, tmp_pvalue < 0.05)){
      potential_HGT[i] = paste0(strsplit(bee_dir[4], './/', fixed=T)[[1]][2], '/', honey_files[gene_fam])
      i = i+1
    }
  }
}

dev.off()



### Bumble and Honey specific plots
pdf('Bumble_Honey_taxo_plot.pdf')

for (gene_fam in 1:length(bumble_honey_files)){
  tmp_file = try(read.table(paste0(bee_dir[3], '/', bumble_honey_files[gene_fam]), sep = '\t'),TRUE)
  if(class(tmp_file) != 'try-error'){
    
    perc_identity = c()
    dist_taxo = c()
    
    for (specie in 1:dim(tmp_file)[1]){
      perc_identity[specie] = tmp_file[specie,3]
      dist_taxo[specie] = taxo_hierarchical$V3[taxo_hierarchical$V1 == strsplit(as.character(tmp_file[specie,2]),
                                                                                '|', fixed = T)[[1]][2]]
    }
    
    for_model = data.frame(xvals = dist_taxo, yvals = perc_identity)
    
    fit = lm(yvals ~ xvals + I(xvals^2), data = for_model)
    fit2 = lm(yvals ~ xvals, data = for_model)
    
    prd = data.frame(xvals = seq(from = 1, to = 10, length.out = 100))
    prd$predicted = predict(fit, newdata = prd)
    
    plot(for_model$xvals, for_model$yvals, main = paste0(strsplit(bee_dir[3], './/', fixed = T)[[1]][2],
                                                         '\n', strsplit(bumble_honey_files[gene_fam],'_parsed')[[1]][1]),
                                                          ylab = 'similarity [%]', xlab = 'hierarchical taxonomy distance [-]', xlim=range(1:7))
    
#    if(class(try(abline(fit2),TRUE)) != 'try-error'){
#      lines(prd$xvals, prd$predicted)
#      abline(fit2)
#    }
    
    tmp_pvalue = anova(fit, fit2)$Pr[2]
    
    if(all(is.na(tmp_pvalue) != TRUE, tmp_pvalue < 0.05)){
      potential_HGT[i] = paste0(strsplit(bee_dir[3], './/', fixed=T)[[1]][2], '/', bumble_honey_files[gene_fam])
      i = i+1
    }
  }
}

dev.off()

write(potential_HGT, file = 'potential_HGT.txt')
