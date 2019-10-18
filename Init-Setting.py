#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 17:31:18 2019

@author: ya
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Define global vaiable and initialization
@author: yaliu
"""
def init():
    #four cases: 1.collapse with copper 2. swell with EDTA
#            3. collapse with copper + 2 fibers
#            4. swell with EDTA + 2 fibers
#            5. collapse with copper + four fibers
    global CASELABEL, ALLMONOMER, GEL,GELCROSSLINK,GELDANGLE,TOPWALL,BOTTOMWALL
    global BINDINGSITE, COPPER, EDTA
    global COMPLEX_BIND, COMPLEX_COPPER, COMPLEX_EDTA, FIBER_TETHER
    global FIBER_JOINT, FIBER_JOINT2,FIBER_HEAD1, FIBER_HEAD2, FIBER_HEAD3, FIBER_HEAD4
    global timestep, res, num_free_site, num_free_copper, num_free_edta, num_complex_site
    global num_complex_copper, num_complex_edta, height_fiber, gyration_fiber
    global test_count
    CASELABEL = 1
    #read file to array
    ALLMONOMER = []
    GEL = []
    GELCROSSLINK =[]
    GELDANGLE = []
    TOPWALL = []
    BOTTOMWALL = []
    BINDINGSITE = []
    COPPER = []
    EDTA = []
    COMPLEX_BIND = []
    COMPLEX_COPPER = []
    COMPLEX_EDTA = []
    FIBER_TETHER = []
    FIBER_JOINT = []
    FIBER_JOINT2 = []
    FIBER_HEAD1 = []
    FIBER_HEAD2 = [] 
    FIBER_HEAD3 = []
    FIBER_HEAD4 = []

    #global parameter
    timestep = 0 
    res = [0,0] #gel surface height: mean & std
    num_free_site = 0
    num_free_copper = 0
    num_free_edta = 0
    num_complex_site = 0
    num_complex_copper = 0
    num_complex_edta = 0
    height_fiber = 0.
    gyration_fiber = 0.
    test_count = 0
     

def clear_array():
    Setting.ALLMONOMER = []
    Setting.GEL = []
    Setting.GELCROSSLINK =[]
    Setting.GELDANGLE = []
    Setting.TOPWALL = []
    Setting.BOTTOMWALL = []
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
  
                