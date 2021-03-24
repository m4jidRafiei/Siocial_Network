from Utilities import Utilities
from SNCreator import SNCreator
import numpy as np
import pandas as pd


import os
from pm4py.objects.log.importer.xes import factory as xes_importer_factory

log = xes_importer_factory.apply("./event_logs/BPI Challenge 2017_App.xes")

utils = Utilities(log)

if not os.path.exists("./intermediate_dataframe"):
    os.makedirs("./intermediate_dataframe")

if not os.path.exists("./intermediate_matrices"):
    os.makedirs("./intermediate_matrices")



snFull_DF, resourceList, activityList = utils.create_full_matrix_next(log)
snFull_DF.to_csv("./intermediate_dataframe/ListFullHashed.csv", sep=',', encoding='utf-8')

snCrt_Full = SNCreator(resourceList, activityList, snFull_DF)

ActActMatrix_handover = snCrt_Full.makeHandoverMatrix(attribute='activity')

ActActMatrix_handover_org = pd.DataFrame(ActActMatrix_handover, index=activityList, columns=activityList)
ActActMatrix_handover_org.to_csv("./intermediate_matrices/ActActMatrix_2017_handover.csv", sep=',', encoding='utf-8')


snCrt_Full.drawRscRscGraph_advanced(ActActMatrix_handover,0, True, False, labels='activity')


