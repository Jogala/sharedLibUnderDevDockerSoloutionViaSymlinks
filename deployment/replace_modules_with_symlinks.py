#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 18:45:02 2021

@author: jrosenberger
"""

import os
import shutil
import pickle

#%%
with open ('symlinksReplacedWithModules_paths.pkl', 'rb') as file:
    srcDestPaths = pickle.load(file)

#%%
for [pathSrc,pathDest] in srcDestPaths:
    
    print('removing module ',pathDest)
    shutil.rmtree(pathDest)
    
    if(pathSrc.split('../')[0] == ''):
        print('relative path ',pathDest)
        pathSrc = '../' + pathSrc
    else:
        print('absolute path ',pathSrc)
        pass
    
    print('inserting symlink ',pathDest)
    os.symlink(pathSrc,pathDest)
    
    