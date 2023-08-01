# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 23:44:21 2023

@author: rkumar0am
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

plt.style.use('dark_background')

import os

def exploreInputs():
    for dirname,_, filenames in os.walk('./input'):
        for filename in filenames:
            print(filename)
            
exploreInputs()       
