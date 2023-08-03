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
    BASE = './input/'

    train = pd.read_csv(BASE + "train.csv")
    test = pd.read_csv(BASE + "test.csv")
    oil = pd.read_csv(BASE + "oil.csv")
    stores = pd.read_csv(BASE + "stores.csv")
    transactions = pd.read_csv(BASE + "transactions.csv")
    holidays_events = pd.read_csv(BASE + "holidays_events.csv")
    sample_submission = pd.read_csv(BASE + "sample_submission.csv") 
        
exploreInputs()       

#Preprocessing of inputData
