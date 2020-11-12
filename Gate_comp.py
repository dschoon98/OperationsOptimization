import numpy as np
import os
import pandas as pd
import time
from gurobipy import Model,GRB,LinExpr
import pickle
from copy import deepcopy


cwd = os.getcwd()
# instance name
instance_name = 'dataset.xlsx'
startTimeSetUp = time.time()
model = Model()
# Load data for this instance
edges  = pd.read_excel(os.path.join(cwd,instance_name),sheet_name='new_format')




########## Creating Gate Compatability Matrix ##############
n_gates = 4
gate_comp = np.zeros((len(edges), n_gates))
cost = np.zeros((len(edges), n_gates))

for i in range(0, len(edges)):
    for j in range(0, n_gates):
        cost[i][j] = edges["Gate %s"%(j+1)][i]
        if edges["Gate %s"%(j+1)][i] != 0:
            gate_comp[i][j] = 1
        
