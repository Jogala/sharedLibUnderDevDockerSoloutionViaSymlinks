#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 16:46:18 2021

@author: jrosenberger
"""

#!/bin/bash

import sys
import os
import shutil
import subprocess
import pickle


pathsModuls = ['../myapp/']

for pathModul in pathsModuls:
    
    print(pathModul)
    
    cmd = "find " + pathModul + "node_modules -maxdepth 1 -type l -ls"
    process = subprocess.Popen(cmd.split(' '), stdout=subprocess.PIPE)
    output, error = process.communicate()
    smylinkModules = output.decode('ascii').split('\n')
    smylinkModules = [ele for ele in smylinkModules if len(ele)]
    
    locationSymlink=[ele.split(' ')[::-1][2] for ele in smylinkModules]
    originalLocation = [ele.split(' ')[::-1][0] for ele in smylinkModules]
    
    print('symlinnks found in ',pathModul + 'node_modules',':')
    print(locationSymlink)
    
    #remove symlinks from node_modules
    print('\n removing symlinks:')
    for path in locationSymlink:
        print(path)
        os.unlink(path)
    print()
        
    #%%
    #copy original modules into node_modules
    
    srcDestPaths = []
    
    for i in range(len(locationSymlink)):
        
        pathDest = locationSymlink[i]
        pathSrc = originalLocation[i]
        
        if(len(pathSrc.split('../')) == 2 and pathSrc.split('../')[1] == ''):
            raise("Relativ Path to module has to be within same project!")
    
        
        if(pathSrc.split('../')[0] == ''):
            print('relative path ',pathDest)
            pathSrc = '../'.join(pathSrc.split('../')[1::])
        else:
            print('absolute path ',pathSrc)
            pass
    
    
        print('copy ',pathSrc,' to ',pathDest)
        print()
        shutil.copytree(pathSrc, pathDest)
        srcDestPaths.append([pathSrc,pathDest])

#%%
with open('symlinksReplacedWithModules_paths.pkl', 'wb') as file:
    pickle.dump(srcDestPaths, file)

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
    
    
    
    
    
    
    
