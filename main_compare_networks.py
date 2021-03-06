'''
Created on Feb 27, 2019

@author: majid
'''
import pandas as pd
from scipy.stats import pearsonr
import numpy as np
from statistics import mean 
import math


def accuracy_analysis(original_adjacentMatrix, modified_adjacentMatrix, threshold_scale):
    
    for Threshold in np.arange(0.0, 1.0, threshold_scale):  
        print(Threshold)
        print('============================') 
        rows, cols = np.where(original_adjacentMatrix > Threshold)
        list_tuple_original = zip(rows, cols)
        list_tuple_original = list(list_tuple_original)
        
        rows, cols = np.where(modified_adjacentMatrix > Threshold)
        list_tuple_modified = zip(rows, cols)
        list_tuple_modified = list(list_tuple_modified)
        
        counter = 0
        for item in list_tuple_original:
            if(item in list_tuple_modified):
                counter += 1
        
        original_modified = counter/2
        
        original = len(list_tuple_original) / 2
        
        print('Similarity Connected')
        print(original_modified/original)
        
        #unconnected----------------------------------------------------------
        
        rows, cols = np.where(original_adjacentMatrix <= Threshold)
        list_tuple_original = zip(rows, cols)
        list_tuple_original = list(list_tuple_original)
        
        rows, cols = np.where(modified_adjacentMatrix <= Threshold)
        list_tuple_modified = zip(rows, cols)
        list_tuple_modified = list(list_tuple_modified)
        
        counter = 0
        for item in list_tuple_original:
            if(item in list_tuple_modified):
                counter += 1
        
        original_modified = counter/2
        
        original = len(list_tuple_original) / 2
        
        print('Similarity unconnected')
        print(original_modified/original)
        
        print('=================================')
        
# Main is here


df_internal = pd.read_csv("RscRscMatrix_internal_org.csv")
df_external = pd.read_csv("RscRscMatrix_internal.csv")
original_adjacentMatrix = df_internal.iloc[:,1:]
modified_adjacentMatrix = df_external.iloc[:,1:]

accuracy_analysis(original_adjacentMatrix, modified_adjacentMatrix, 0.2)
