#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 14:20:57 2019

@author: yaliu
"""

import pysftp
cnopts = pysftp.CnOpts()
cnopts.hostkeys = None      
srv = pysftp.Connection(host="ya-pc.engr.pitt.edu", username="ya",password="ybl7p-gj",cnopts=cnopts)
remotefolder ='/home/ya/Desktop/Project/Current_Project/code/Gel-Ion-XYZ/Data/Stage2-Copper-Gel-Collapse/HydroSite792-2/C'
localfolder = '/Users/yaliu/Desktop/Project/Code/2-Gel-Ion-XYZ/Data/'
sname = '150-'
for adname in ['1','2','3','4','5','6','7','8','9','10']:
    crf1 = remotefolder+sname+adname+'/config.xyz'
    #crf2 = remotefolder+sname+adname+'/density.txt'
    crf3 = remotefolder+sname+adname+'/stat.txt'
    #newname1 = localfolder+sname+adname+'config.xyz'
    newname2 = localfolder+sname+adname+'density.txt'
    newname3 = localfolder+sname+adname+'stat.txt'
    #if adname== '1':
    #    clf1 = open(newname1,'wb')
    #    srv.getfo(crf1,clf1)
    #clf2 = open(newname2,'wb')
    clf3 = open(newname3,'wb')
    #srv.getfo(crf1,clf1)
    #srv.getfo(crf2,clf2)
    srv.getfo(crf3,clf3)
    #clf1.close()
    #clf2.close()
    clf3.close()