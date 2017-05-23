#!/usr/bin/Rscript


# Claivaz, Ricci, 170516
# This  script allows the plotting of the similarity amongst blast hit results in function of the hierarchical 
# taxonomy distance.
# Input: hierarchical_taxonomy.txt, bumble/honey/bumble&honey parsed blast
# Output: plots and table containing potential HGT candidates (from the anova test between polynomial and linear model)


setwd('/scratch/beegfs/monthly/mls_2016/claivaz_ricci/SAGE_Firm5_specific_HGT/data/parsed_blast')

#Load hierarchical taxonomy and list all out files from parsed blast
taxo_hierarchical = read.table('hierarchical_taxonomy.txt', sep = '\t')
bee_dir = list.dirs('./')
bumble_files = list.files(bee_dir[2])
honey_files = list.files(bee_dir[4])
bumble_honey_files = list.files(bee_dir[3])
#

i = 1
potential_HGT = c()
#plot all files of bumble
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
                                                        ylab='similarity [%]', xlab='hierarchical taxonomy distance [-]')

    if(class(try(abline(fit2),TRUE)) != 'try-error'){
      lines(prd$xvals, prd$predicted)
      abline(fit2)
    }
    
    
    
    tmp_pvalue = anova(fit, fit2)$Pr[2]
    
    if(all(is.na(tmp_pvalue) != TRUE, tmp_pvalue<0.05)){
      potential_HGT[i] = paste0(strsplit(bee_dir[2], './/', fixed=T)[[1]][2], '/', bumble_files[gene_fam])
      i = i+1
    }
  }
}

dev.off()

#plot all files of honey
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
                                                        ylab = 'similarity [%]', xlab = 'hierarchical taxonomy distance [-]')

    if(class(try(abline(fit2),TRUE)) != 'try-error'){
      lines(prd$xvals, prd$predicted)
      abline(fit2)
    }
    
    tmp_pvalue = anova(fit, fit2)$Pr[2]
    
    if(all(is.na(tmp_pvalue) != TRUE, tmp_pvalue < 0.05)){
      potential_HGT[i] = paste0(strsplit(bee_dir[4], './/', fixed=T)[[1]][2], '/', honey_files[gene_fam])
      i = i+1
    }
  }
}

dev.off()

#plot all files of bumble and honey
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
    
    if(class(try(abline(fit2),TRUE)) != 'try-error'){
      lines(prd$xvals, prd$predicted)
      abline(fit2)
    }
    
    tmp_pvalue = anova(fit, fit2)$Pr[2]
    
    if(all(is.na(tmp_pvalue) != TRUE, tmp_pvalue < 0.05)){
      potential_HGT[i] = paste0(strsplit(bee_dir[3], './/', fixed=T)[[1]][2], '/', bumble_honey_files[gene_fam])
      i = i+1
    }
  }
}

dev.off()

write(potential_HGT, file = 'potential_HGT.txt')
