'''
Created on Mar 27, 2019

@author: majid
'''

from pm4py.algo.enhancement.sna import factory as sna_factory
from pm4py.objects.log.importer.xes import factory as xes_importer_factory
from pm4py.visualization.sna import factory as sna_vis_factory


log = xes_importer_factory.apply("Sn_Artificial.xes")


ja_values = sna_factory.apply(log, variant="jointactivities")

gviz_ja_py = sna_vis_factory.apply(ja_values, variant="pyvis")
sna_vis_factory.view(gviz_ja_py, variant="pyvis")






