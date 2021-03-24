'''
Created on Oct 26, 2018

@author: majid
'''
from pm4py.objects.log.importer.xes import factory as xes_importer_factory
from pm4py.objects.log.exporter.xes import factory as xes_exporter
from Utilities import Utilities
from SNCreator import SNCreator
import pandas as pd
import os

log_name = "./event_logs/BPI Challenge 2017_App_minutes_5_60_0.2_relative.xes"
# log_name = "Sn_Artificial_Paper.xes"
log = xes_importer_factory.apply(log_name)

if not os.path.exists("./intermediate_dataframe"):
    os.makedirs("./intermediate_dataframe")

if not os.path.exists("./intermediate_matrices"):
    os.makedirs("./intermediate_matrices")

utils = Utilities(log)

snBasic_DF, resourceList = utils.create_basic_matrix()                  #ICS
# snBasic_DF_Enc, resourceList_Enc = utils.resourceEncryption(snBasic_DF)     #ECS

snBasic_DF.to_csv("./intermediate_dataframe/ListBasic.csv", sep=',', encoding='utf-8')
# snBasic_DF_Enc.to_csv("ListBasicEnc.csv", sep=',', encoding='utf-8')

# snCrtBasic = SNCreator(resourceList_Enc, [] , snBasic_DF_Enc)
snCrtBasic = SNCreator(resourceList, [] , snBasic_DF)

RscRscMatrix_handover = snCrtBasic.makeHandoverMatrix()

RscRscMatrix_handover_org = pd.DataFrame(RscRscMatrix_handover, index=resourceList, columns=resourceList)
RscRscMatrix_handover_org.to_csv("./intermediate_matrices/RscRscMatrix_2017_handover_strong_rel.csv", sep=',', encoding='utf-8')


# resourceList_Dec = utils.resourceDecryption(resourceList_Enc)
# snCrtBasic.setResourceList(resourceList_Dec)


# snCrtBasic.drawRscRscGraph_simple(RscRscMatrix_handover, 0, False)

snCrtBasic.drawRscRscGraph_advanced(RscRscMatrix_handover,0, True, False)

