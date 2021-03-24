'''
Created on Feb 27, 2019

@author: majid
'''
import pandas as pd
from Compare import Compare

original_adjacentMatrix = pd.read_csv("./intermediate_matrices/RscRscMatrix_2017_handover.csv", index_col=0)
modified_adjacentMatrix = pd.read_csv("./intermediate_matrices/RscRscMatrix_2017_handover_strong_rel.csv", index_col=0)

steps = 0.2
compare = Compare()
# compare.compare_equal_nodes(original_adjacentMatrix, modified_adjacentMatrix, steps)

frequency_based = True
connected, unconnected = compare.compare_not_equal_nodes(original_adjacentMatrix, modified_adjacentMatrix, frequency_based)

