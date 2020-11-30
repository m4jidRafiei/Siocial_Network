'''
Created on Oct 26, 2018

@author: majid
'''

from Utilities import Utilities
from SNCreator import SNCreator
import os
from pm4py.objects.log.importer.xes import factory as xes_importer_factory

# log = xes_importer_factory.apply("Sn_Artificial.xes")
# log_name = "BPI_Challenge_2012_APP_anon_minutes_2_20_1_0.8_set.xes"
log_name = "Sn_Artificial_Paper.xes"
log = xes_importer_factory.apply(log_name)

utils = Utilities(log)

if not os.path.exists("./intermediate_dataframe"):
    os.makedirs("./intermediate_dataframe")

if not os.path.exists("./intermediate_matrices"):
    os.makedirs("./intermediate_matrices")

# snFull_DF_hashed, resourceList, activityListHashed = utils.create_full_matrixHashed()
snFull_DF_hashed, resourceList, activityList = utils.create_full_matrix()

# snFull_DF_Enc, resourceList_Enc = utils.resourceEncryption(snFull_DF_hashed)     #ECS


snFull_DF_hashed.to_csv("./intermediate_dataframe/ListFullReal.csv", sep=',', encoding='utf-8')
# snFull_DF_Enc.to_csv("ListFullRealEnc.csv", sep=',', encoding='utf-8')


# snCrtFull = SNCreator(resourceList_Enc, activityListHashed , snFull_DF_Enc)
# snCrtFull = SNCreator(resourceList, activityListHashed , snFull_DF_hashed)
snCrtFull = SNCreator(resourceList, activityList , snFull_DF_hashed)


RscRscMatrix_handover = snCrtFull.makeRealHandoverMatrix(0)


# resourceList_Dec = utils.resourceDecryption(resourceList_Enc)
# snCrtBasic.setResourceList(resourceList_Dec)


# snCrtBasic.drawRscRscGraph_simple(RscRscMatrix_handover, 0, False)

snCrtFull.drawRscRscGraph_advanced(RscRscMatrix_handover,0, True, False)

