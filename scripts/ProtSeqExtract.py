# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 16:01:44 2017

@author: Claivaz & Ricci

Function which extract the amino sequence of the defined ortholog create by subgroup_sort_if_only_L185_for_out_lacto.py
"""
import os
import re
from glob import glob
os.getcwd()
os.chdir('D:\\Unil\Master\Semester 2\SAGE\project')


def extract_aa_set(file_set,directory_path_file_set,directory_path_file_faa):
    import os
    import re
    from glob import glob

    f_set=open(directory_path_file_set+'\\'+file_set,'r') #open the right set file
    f_set_out=open(directory_path_file_set+'\\'+file_set.split('.')[0]+'_out.txt','w') #create the output file
    
    New_aa=False
    
    tmp=glob(directory_path_file_faa+'\\'+'*.faa') #list all the file containing the extension .faa
    files_faa=[]
    for i in tmp:
        files_faa.append(i.split('\\') [-1])

    for g_fam_tmp in f_set:
        g_fam=g_fam_tmp.split('\t')
        for strain in g_fam:
            if strain.split('_')[0]!='Gene' and strain!='' and strain!='\n':
                if strain.split('|')[0]+'.faa' in files_faa:
                    read_file=open(directory_path_file_faa+'\\'+"%s.faa" %strain.split('|')[0],'r')
                    for line in read_file:
                            if New_aa :
                                if line.split('|')[0]=='>fig' :
                                    New_aa=False
                                    break
                                else:
                                    f_set_out.write(line.replace('\n',''))
                            if re.search(strain.split('|')[1]+'\n',line):
                                New_aa=True
                                f_set_out.write(' | ' + strain.split('|')[0] + ' | ')
                    read_file.close()
            elif strain.split('_')[0]=='Gene':
                f_set_out.write(' | ' + strain + ' | ')
    f_set_out.close()
        
#Run function in all set files
from glob import glob
tmp=glob('D:\\Unil\Master\Semester 2\SAGE\project\set*')
files_set=[]
for i in tmp:
    files_set.append(i.split('\\') [-1])
for i in files_set:
    extract_aa_set(file_set=i,directory_path_file_set='D:\\Unil\Master\Semester 2\SAGE\project',directory_path_file_faa='D:\\Unil\Master\Semester 2\SAGE\project\RastOut_ProtSeq')            
        
