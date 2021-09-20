# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

pathsModuls = ['../myapp/'] 

import json
import copy
import os

for pathModul in pathsModuls:

    os.copy(pathModul + 'package.json',pathModul + 'package_tmp.json')
     
    with open(pathModul + 'package.json','r') as f:
        packages = json.load(f) 
    
    packagesNotLocal = copy.deepcopy(packages)
    for key in packages["dependencies"]:
        val = packages["dependencies"][key]
        if(val[0:5] == 'file:'):
            print('removing ',val)
            del packagesNotLocal["dependencies"][key]
            
    
    with open(pathModul + 'package.json','w') as f:
        json.dump(packagesNotLocal, f, ensure_ascii=False, indent=4)
