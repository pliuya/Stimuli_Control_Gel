#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 16:47:05 2019
1.from dump file, extract xyz for each time frame
2. for each time frame, get statistic:
   gel height + number free copper + open binding site + single binding + double binding  
@author: yaliu
"""
import sys
if 'GFunc' in sys.modules:  
    del sys.modules["GFunc"]
if 'Setting' in sys.modules:  
    del sys.modules["Setting"]


import numpy as np
import pandas as pd
import GFunc
import Setting

#initialize global variable
Setting.init()
#input, output file
filedirectory = '/Users/yaliu/Desktop/Project/Code/2-Gel-Ion-XYZ/Data/'
inputfilename = filedirectory+'dump.lammpstrj'
outputfilenamexyz = filedirectory +'config.xyz'
outputfilenamestat = filedirectory +'stat.txt'

inputfile=open(inputfilename,'r')
outputfile_xyz = open(outputfilenamexyz,'w+')
outputfile_stat = open(outputfilenamestat,'w+')

#SYSTEM PARAMETERS
SYSTEMSIZE = [24.6411, 24.6411, 50.]

#Color Map



#read file, extract information
#set check point in file
is_Time = False
is_Coord = False
is_Calc = False  
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
while True:
    line = inputfile.readline()
    if len(line) == 0:
        print('a1: No input file/empty input file/finish input')
        break         
    if line.split()[0] == 'ITEM:' and line.split()[1] == 'TIMESTEP':
        is_Time = True
        if is_Calc == True: 
            print('Time Step: {0}'.format(Setting.timestep))
            Setting.num_free_site = len(Setting.BINDINGSITE)
            Setting.num_free_copper = len(Setting.COPPER)
            Setting.num_free_edta = len(Setting.EDTA)
            Setting.num_complex_site = len(Setting.COMPLEX_BIND)
            Setting.num_complex_copper = len(Setting.COMPLEX_COPPER)
            Setting.num_complex_edta = len(Setting.COMPLEX_EDTA)
            Setting.res = GFunc.gel_surface(Setting.GEL,SYSTEMSIZE[0],num_grid = 10)
            GFunc.stat_fiber()        
            GFunc.print_stat(outputfile_stat)
            GFunc.print_xyz(outputfile_xyz)
            GFunc.clear_array()
            is_Coord = False
            is_Calc = False
            if Setting.timestep == 4995000:
                bind_density(Setting.COMPLEX_COPPER,Setting.num_complex_copper,Setting.res[0],5)
        continue
    #Get time step
    if is_Time == True:
        Setting.timestep = int(line.split()[0])
        is_Time = False
        continue 
    if line.split()[0] == 'ITEM:' and line.split()[1] == 'ATOMS':
        is_Coord = True
        continue
#Get coordinate
    if  is_Coord == True:
        is_Calc = True
        if(len(line.split())<6):
            raise SystemExit('Data missing;stop code')
        mono_index = int(line.split()[0])
        mono_type = int(line.split()[1])
        mono_id = int(line.split()[2])
        mono_x = float(line.split()[3])
        mono_y = float(line.split()[4])
        mono_z = float(line.split()[5])
        mono_coord = [mono_x,mono_y,mono_z]
        if mono_type == 4 or mono_type == 5:
            Setting.WALL.append(mono_coord)
        elif mono_type <= 3:
            Setting.GEL.append(mono_coord)
        elif mono_type == 7:
            Setting.BINDINGSITE.append(mono_coord)
        elif mono_type == 8:
            Setting.COPPER.append(mono_coord)
        elif mono_type == 9: 
            Setting.COMPLEX_BIND.append(mono_coord)
        elif mono_type == 10: 
            Setting.COMPLEX_COPPER.append(mono_coord)
        elif mono_type == 11: 
            if Setting.CASELABEL == 2:
                Setting.EDTA.append(mono_coord)
            elif Setting.CASELABEL == 3 or Setting.CASELABEL == 5:
                Setting.FIBER_TETHER.append(mono_coord)
        elif mono_type == 12:
            if Setting.CASELABEL == 2:
                Setting.COMPLEX_EDTA.append(mono_coord)
            if Setting.CASELABEL == 3 and Setting.CASELABEL == 5:
                Setting.FIBER_JOINT.append(mono_coord)  
        elif mono_type == 13: 
            if Setting.CASELABEL == 3:
                Setting.FIBER_HEAD1.append(mono_coord) 
            if Setting.CASELABEL == 5:
                Setting.FIBER_JOINT2.append(mono_coord)
        elif mono_type == 14:        
            if Setting.CASELABEL == 3:
                Setting.FIBER_HEAD2.append(mono_coord) 
            if Setting.CASELABEL == 5:
                Setting.FIBER_HEAD1.append(mono_coord)
        elif mono_type == 15:
                Setting.FIBER_HEAD2.append(mono_coord) 
        elif mono_type == 16:
                Setting.FIBER_HEAD3.append(mono_coord)         
        elif mono_type == 17:
                Setting.FIBER_HEAD4.append(mono_coord)         
#close file
inputfile.close()
outputfile_xyz.close()
outputfile_stat.close() 
                
                
                
                