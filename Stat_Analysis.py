#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 15:27:49 2019

@author: yaliu
"""

import numpy as np
localfolder = '/Users/yaliu/Desktop/Project/Code/2-Gel-Ion-XYZ/Data/'
sname = '150-'

num_row = 10
all_data = []

each_line = [0 for i in range(num_row)]
file_index = 0 
for adname in ['1','2','3','4','5','6','7','8','9','10']:
    name_stat = localfolder+sname+adname+'stat.txt'
    tempfile = open(name_stat,'r')
    each_file_data = []
    print('Read file {0}'.format(adname))
    while True:
        input = tempfile.readline()
        if len(input)==0:
            break
        for i in range(num_row):
            if i in [1,num_row-2,num_row-1]:
                each_line[i]=float(input.split()[i])
            else:
                each_line[i]=int(input.split()[i])    
        each_file_data.append(each_line[:])
    
    print('File {0} size is {1}\n'.format(adname,len(np.transpose(each_file_data)[0])))
    all_data.append(np.transpose(each_file_data)[:])
    
    print('Total File size is {}\n'.format(len(np.transpose(all_data)[0])))
    tempfile.close()
