#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 13:29:34 2021

@author: jrosenberger
"""

pathsModuls = ['../myapp/'] 

import shutil

for pathModul in pathsModuls:
    print(pathModul + 'package_tmp.json',' -> ',pathModul + 'package.json')
    shutil.move(pathModul + 'package_tmp.json',pathModul + 'package.json')
