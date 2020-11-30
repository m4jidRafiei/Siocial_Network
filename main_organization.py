'''
Created on Oct 26, 2018

@author: majid
'''

from Utilities import Utilities
from SNCreator import SNCreator
import numpy as np
import pandas as pd


import os
from pm4py.objects.log.importer.xes import factory as xes_importer_factory

log = xes_importer_factory.apply("Sn_Artificial_Paper.xes")

utils = Utilities(log)

if not os.path.exists("./intermediate_dataframe"):
    os.makedirs("./intermediate_dataframe")

if not os.path.exists("./intermediate_matrices"):
    os.makedirs("./intermediate_matrices")



snFull_DF_hashed, resourceList, activityListHashed = utils.create_full_matrix_next(log)


snFull_DF_hashed.to_csv("./intermediate_dataframe/ListFullHashed.csv", sep=',', encoding='utf-8')



snCrt_Full_Hashed = SNCreator(resourceList, activityListHashed, snFull_DF_hashed)

RscActMatrix_jointactivities = snCrt_Full_Hashed.makeJointActivityMatrix_next()

RscActMatrix_jointactivities_pd = pd.DataFrame(RscActMatrix_jointactivities, index=resourceList, columns=activityListHashed)
RscActMatrix_jointactivities_pd.to_csv("./intermediate_matrices/RscActMatrix_jointactivities_internal.csv", sep=',', encoding='utf-8')

# RscRscMatrix_jointactivities = snCrt_Full_Hashed.convertRscAct2RscRsc(RscActMatrix_jointactivities, "pearson")
RscRscMatrix_jointactivities = snCrt_Full_Hashed.convertRscAct2RscRsc(RscActMatrix_jointactivities, "pearson")
#convert triangular to symmetric
i_lower = np.tril_indices(RscRscMatrix_jointactivities.shape[0], -1)
RscRscMatrix_jointactivities[i_lower] = RscRscMatrix_jointactivities.T[i_lower]  # make the matrix symmetric

RscRscMatrix_jointactivities_pd = pd.DataFrame(RscRscMatrix_jointactivities, index=resourceList, columns=resourceList)
RscRscMatrix_jointactivities_pd.to_csv("./intermediate_matrices/RscRscMatrix_internal_org.csv", sep=',', encoding='utf-8')


# first_act_frq = utils.get_activity_frequency(snFull_DF_hashed)
# first_act_frq.to_csv("first_act_frq.csv", sep=',', encoding='utf-8')


snCrt_Full_Hashed.drawRscRscGraph_advanced(RscRscMatrix_jointactivities, 0.2, False, False)



