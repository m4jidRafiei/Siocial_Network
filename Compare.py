import pandas as pd
from scipy.stats import pearsonr
import numpy as np
from statistics import mean
import math


class Compare:

    def __init__(self):
        self = self

    def compare_equal_nodes(self,original_adjacentMatrix, modified_adjacentMatrix, steps):
        # original_adjacentMatrix = original_adjacentMatrix.iloc[:, 1:]
        # modified_adjacentMatrix = modified_adjacentMatrix.iloc[:, 1:]

        for Threshold in np.arange(0.0, 1.0, steps):
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
                if (item in list_tuple_modified):
                    counter += 1

            original_modified = counter / 2

            original = len(list_tuple_original) / 2

            print('Similarity Connected')
            print(original_modified / original)

            # unconnected----------------------------------------------------------

            rows, cols = np.where(original_adjacentMatrix <= Threshold)
            list_tuple_original = zip(rows, cols)
            list_tuple_original = list(list_tuple_original)

            rows, cols = np.where(modified_adjacentMatrix <= Threshold)
            list_tuple_modified = zip(rows, cols)
            list_tuple_modified = list(list_tuple_modified)

            counter = 0
            for item in list_tuple_original:
                if (item in list_tuple_modified):
                    counter += 1

            original_modified = counter / 2

            original = len(list_tuple_original) / 2

            print('Similarity unconnected')
            print(original_modified / original)

            print('=================================')

    def compare_not_equal_nodes(self,original_adjacentMatrix, modified_adjacentMatrix,frequency_based):
        # fitness or connnected part
        connected_modified  = 0
        connected_original = 0
        unconnected_modified  = 0
        unconnected_original = 0
        for column in original_adjacentMatrix.columns:
                for index in original_adjacentMatrix.index.values.tolist():
                    if original_adjacentMatrix.loc[index,column] > 0:
                        if column in modified_adjacentMatrix.columns and index in modified_adjacentMatrix.index.values.tolist():
                            if frequency_based:
                                connected_modified += modified_adjacentMatrix.loc[index,column]
                            else:
                                connected_modified += 1
                        if frequency_based:
                            connected_original += original_adjacentMatrix.loc[index,column]
                        else:
                            connected_original += 1
                    elif original_adjacentMatrix.loc[index,column] == 0:
                        unconnected_original += 1
                        if column in modified_adjacentMatrix.columns and index in modified_adjacentMatrix.index.values.tolist():
                            if modified_adjacentMatrix.loc[index,column] == 0:
                                unconnected_modified += 1
                        else:
                            unconnected_modified += 1
        connected_score = connected_modified / connected_original
        unconnected_score = unconnected_modified / unconnected_original
        f1_score = (2*connected_score*unconnected_score) / (connected_score + unconnected_score)
        print('connected: %f -- unconnected:%f -- f1_score:%f' %(connected_score,unconnected_score,f1_score))
        return connected_score, unconnected_score

