#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Def function for Configu-XYZ.py
@author: yaliu
"""
import sys
if 'Setting' in sys.modules:  
    del sys.modules["Setting"]
import numpy as np
import Setting 

def gel_surface(gel_coord,sys_size,num_grid):
    grid_size = sys_size/num_grid
    Surf_Matrix = [[0 for x in range(num_grid+1)] for y in range(num_grid+1)]
    for temp_coord in gel_coord:
        grid_x = int(temp_coord[0]/grid_size)
        grid_y = int(temp_coord[1]/grid_size)
        if temp_coord[2] > Surf_Matrix[grid_x][grid_y]:
            Surf_Matrix[grid_x][grid_y] = temp_coord[2]
    Surf_Array = np.array(Surf_Matrix).ravel()
    avg_height = np.mean(Surf_Array)
    std_height = np.std(Surf_Array)
    rv = [avg_height,std_height]
    return rv


def bind_density(complex_coord,t_num,sys_size,num_grid):
    #sys_size is the maximum of gel height, num_grid = 5
    tempdirectory = '/Users/yaliu/Desktop/Project/Code/2-Gel-Ion-XYZ/Data/'
    outputname = tempdirectory +'density.txt'

    outputfile_density = open(outputname,'w+')
    
    grid_size = sys_size/num_grid
    density_Array = [0 for x in range(num_grid+1)] 
    for temp_coord in complex_coord:
        grid_z = int(temp_coord[2]/grid_size)
        density_Array[grid_z] += 1
    for i in range(num_grid+1):
        outputfile_density.write('{0}\t{1}'.format(grid_size*(1+i)/sys_size,density_Array[i]/t_num))
        
def stat_fiber():
    if Setting.CASELABEL < 5 and Setting.CASELABEL >2: #two fibers
       t1 = [x[2] for x in Setting.FIBER_HEAD1]
       t2 = [x[2] for x in Setting.FIBER_HEAD2]
       Setting.height_fiber = (np.max(t1)+ np.max(t2))*0.5
       c = np.array(Setting.FIBER_HEAD1[np.argmax(t1)])
       -np.array(Setting.FIBER_HEAD2[np.argmax(t2)])
       Setting.gyration_fiber = np.sum(np.square(c))**0.5*0.5 # radius
    elif Setting.CASELABEL > 4:
       t1 = [x[2] for x in Setting.FIBER_HEAD1]
       t2 = [x[2] for x in Setting.FIBER_HEAD2]
       t3 = [x[2] for x in Setting.FIBER_HEAD3]
       t4 = [x[2] for x in Setting.FIBER_HEAD4]
       
       Setting.height_fiber = (np.max(t1)+ np.max(t2)+ np.max(t3)+ np.max(t4
                               ))*0.25
       c1 = np.array(Setting.FIBER_HEAD1[np.argmax(t1)])
       -np.array(Setting.FIBER_HEAD3[np.argmax(t3)])
       c2 = np.array(Setting.FIBER_HEAD2[np.argmax(t2)])
       -np.array(Setting.FIBER_HEAD4[np.argmax(t4)])
       Setting.gyration_fiber = np.sum(np.square(c1))**0.5*0.25
       + np.sum(np.square(c2))**0.5*0.25
        
        
def clear_array():
    Setting.GEL = []
    Setting.WALL = []
    Setting.BINDINGSITE = []
    Setting.COPPER = []
    Setting.EDTA = []
    Setting.COMPLEX_BIND = []
    Setting.COMPLEX_COPPER = []
    Setting.COMPLEX_EDTA = []
    Setting.FIBER_TETHER = []
    Setting.FIBER_JOINT = []
    Setting.FIBER_JOINT2 = []
    Setting.FIBER_HEAD1 = []
    Setting.FIBER_HEAD2 = [] 
    Setting.FIBER_HEAD3 = []
    Setting.FIBER_HEAD4 = []

def print_stat(filename):      
    filename.write('{0:7d}\t{1:4f}\t{2:4d}\t{3:4d}\t{4:4d}\t{5:4d}\t{6:4d}\t{7:4d}\t{8:4f}\t{9:4f}\n'.format(
    Setting.timestep, Setting.res[0], Setting.num_free_site, Setting.num_free_copper, 
    Setting.num_free_edta, Setting.num_complex_site, Setting.num_complex_copper, 
    Setting.num_complex_edta, Setting.height_fiber, Setting.gyration_fiber))

    
def print_xyz(filename):
    COLOR_MAP = {1:'H',2:'O',3:'N',4:'C',5:'C',6:'F',7:'K',8:'S',9:'T',10:'Z',11:'P'}
    bead1 = Setting.num_free_site + Setting.num_complex_site
    bead2 = Setting.num_free_copper + Setting.num_complex_copper
    bead3 = Setting.num_free_edta + Setting.num_complex_edta
    if Setting.CASELABEL < 3:
        bead4 = 0
    elif Setting.CASELABEL < 5:
        bead4 = len(Setting.FIBER_TETHER) + len(FIBER_JOINT) + len(FIBER_HEAD1)*2
    elif Setting.CASELABEL > 5:
        bead4 = len(Setting.FIBER_TETHER) + len(FIBER_JOINT)*2 + len(FIBER_HEAD1)*4
    bead5 = len(Setting.GEL)
    bead6 = len(Setting.WALL)
    TotalMono = bead1*2 + bead2*2 + bead3*2 + bead4 + bead5 + bead6
    filename.write('{0:d}\n'.format(TotalMono))
    filename.write('\n'.format('gel ion edta'))
    for item in Setting.GEL:
        filename.write('{0:s}\t{1:6f}\t{2:6f}\t{3:6f}\n'.format(COLOR_MAP[1],item[0],item[1],item[2]))
    for item in Setting.WALL:
        filename.write('{0:s}\t{1:6f}\t{2:6f}\t{3:6f}\n'.format(COLOR_MAP[2],item[0],item[1],item[2]))
    for item in Setting.BINDINGSITE:
        filename.write('{0:s}\t{1:6f}\t{2:6f}\t{3:6f}\n'.format(COLOR_MAP[3],item[0],item[1],item[2]))
    for i in range(Setting.num_complex_site):
        filename.write('{0:s}\t{1:6f}\t{2:6f}\t{3:6f}\n'.format(COLOR_MAP[3],0.,24.6411,0))
    for item in Setting.COPPER:
        filename.write('{0:s}\t{1:6f}\t{2:6f}\t{3:6f}\n'.format(COLOR_MAP[4],item[0],item[1],item[2]))
    for i in range(Setting.num_complex_copper):
        filename.write('{0:s}\t{1:6f}\t{2:6f}\t{3:6f}\n'.format(COLOR_MAP[4],0.,24.6411,0))
    for item in Setting.EDTA:
        filename.write('{0:s}\t{1:6f}\t{2:6f}\t{3:6f}\n'.format(COLOR_MAP[5],item[0],item[1],item[2]))
    for i in range(Setting.num_complex_edta):
        filename.write('{0:s}\t{1:6f}\t{2:6f}\t{3:6f}\n'.format(COLOR_MAP[5],0.,24.6411,0))
 
    for item in Setting.COMPLEX_BIND:
        filename.write('{0:s}\t{1:6f}\t{2:6f}\t{3:6f}\n'.format(COLOR_MAP[6],item[0],item[1],item[2]))
    for i in range(Setting.num_free_site):
        filename.write('{0:s}\t{1:6f}\t{2:6f}\t{3:6f}\n'.format(COLOR_MAP[6],0.,24.6411,0))
    for item in Setting.COMPLEX_COPPER:
        filename.write('{0:s}\t{1:6f}\t{2:6f}\t{3:6f}\n'.format(COLOR_MAP[7],item[0],item[1],item[2]))
    for i in range(Setting.num_free_copper):
        filename.write('{0:s}\t{1:6f}\t{2:6f}\t{3:6f}\n'.format(COLOR_MAP[7],0.,24.6411,0))
    for item in Setting.COMPLEX_EDTA:
        filename.write('{0:s}\t{1:6f}\t{2:6f}\t{3:6f}\n'.format(COLOR_MAP[8],item[0],item[1],item[2]))
    for i in range(Setting.num_free_edta):
        filename.write('{0:s}\t{1:6f}\t{2:6f}\t{3:6f}\n'.format(COLOR_MAP[8],0.,24.6411,0))
    for item in Setting.FIBER_TETHER:
        filename.write('{0:s}\t{1:6f}\t{2:6f}\t{3:6f}\n'.format(COLOR_MAP[9],item[0],item[1],item[2]))
    for item in Setting.FIBER_JOINT:
        filename.write('{0:s}\t{1:6f}\t{2:6f}\t{3:6f}\n'.format(COLOR_MAP[10],item[0],item[1],item[2]))
    for item in Setting.FIBER_JOINT2:
        filename.write('{0:s}\t{1:6f}\t{2:6f}\t{3:6f}\n'.format(COLOR_MAP[10],item[0],item[1],item[2]))
    for item in Setting.FIBER_HEAD1:
        filename.write('{0:s}\t{1:6f}\t{2:6f}\t{3:6f}\n'.format(COLOR_MAP[11],item[0],item[1],item[2]))
    for item in Setting.FIBER_HEAD2:
        filename.write('{0:s}\t{1:6f}\t{2:6f}\t{3:6f}\n'.format(COLOR_MAP[11],item[0],item[1],item[2]))
    for item in Setting.FIBER_HEAD3:
        filename.write('{0:s}\t{1:6f}\t{2:6f}\t{3:6f}\n'.format(COLOR_MAP[11],item[0],item[1],item[2]))
    for item in Setting.FIBER_HEAD4:
        filename.write('{0:s}\t{1:6f}\t{2:6f}\t{3:6f}\n'.format(COLOR_MAP[11],item[0],item[1],item[2]))


        
        
  
    

    
  
                