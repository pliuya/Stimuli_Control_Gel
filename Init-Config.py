#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 14:54:12 2019
#Study swelling dynamics with 2 fibers and 4 fibers
#Prepare initial configure: 1. Collapsing gel + 2 fibers + EDTA 
                            2. Collapsing gel + 4 fibers + EDTA
@author: ya
"""
import sys

if 'Init-Setting' in sys.modules:
    del sys.modules['Init-Setting']
    
import numpy as np
import pandas as pd
import GFunc
import Setting

#Setting.CASELABEL = 1: dump for late stage from 2 fiber collapsing
#Setting.CASELABEL = 2: dump for late stage from 4 fiber collapsing


inputdumpfilename = 'dump.lammpstrj' 
inputfilename = '250-Fiber-Copper-Gel.data'
outputfilename= 'init.2fiber.data'

inputdumpfile = open(inputdumpfilename,'r')
inputfile = open(inputfilename,'r')

writefile = open(outputfilename,'w+')

last_time = 2000*94
time_step = 0
#read file, extract information
#set check point in file
is_Time = False
is_Coord = False
is_Calc = False  
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
while True:
    line = inputdumpfile.readline()
    if len(line) == 0:
        print('a1: No input file/empty input file/finish input')
        break         
    if line.split()[0] == 'ITEM:' and line.split()[1] == 'TIMESTEP':
        is_Time = True
        if is_Calc == True: #generate initial files
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
        continue
    #Get time step
    if is_Time == True:
        Setting.timestep = int(line.split()[0])
        print('Current time step is: {0:d}'.format(Setting.timestep))
        is_Time = False
        continue 
    if line.split()[0] == 'ITEM:' and line.split()[1] == 'ATOMS':
        is_Coord = True
        continue
#Get coordinate
    if  is_Coord == True and  Setting.timestep == last_time:
        is_Calc = True
        if(len(line.split())<6):
            raise SystemExit('Data missing;stop code')
        mono_index = int(line.split()[0])
        mono_type = int(line.split()[1])
        mono_id = int(line.split()[2])
        mono_x = float(line.split()[3])
        mono_y = float(line.split()[4])
        mono_z = float(line.split()[5])
        mono_coord = [mono_index,mono_type,mono_x,mono_y,mono_z]
        Setting.ALLMONOMER.append(mono_coord)
"""       
        if mono_type == 1:
            Setting.GELCROSSLINK.append(mono_coord)
        elif mono_type == 2:
            Setting.GEL.append(mono_coord)
        elif mono_type == 3:
            Setting.GELDANGLE.append(mono_coord)
        elif mono_type == 4: 
            Setting.BOTTOMWALL.append(mono_coord)
        elif mono_type == 5:
            Setting.TOPWALL.append(mono_coord)
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
 """               
print('End of Recording Late Coordinate')

#replace free copper by solvent 
Print('Start Generating Input File')
while True:
    line = inputfile.readline()
    if len(line) == 0:
        print('a1: No input file/empty input file/finish input')
        break 
    