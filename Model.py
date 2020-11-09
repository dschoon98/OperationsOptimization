# Loading packages that are used in the code
import numpy as np
import os
import pandas as pd
import time
from gurobipy import Model,GRB,LinExpr
import pickle
from copy import deepcopy

# Get path to current folder
cwd = os.getcwd()

# Get all instances
full_list           = os.listdir(cwd)

# instance name
instance_name = 'dataset.xlsx'

# Load data for this instance
edges  = pd.read_excel(os.path.join(cwd,instance_name),sheet_name='Python_sheet')

startTimeSetUp = time.time()
model = Model()

#################
### VARIABLES ###
#################
x = {}
for i in range(0,len(edges)):
    x[edges['Flight'][i],edges['Gate'][i]]=model.addVar(lb=0, ub=1, vtype=GRB.BINARY,name="x[%s,%s]"%(edges['Flight'][i],edges['Gate'][i]))

            
model.update()

###################
### CONSTRAINTS ###
###################

for i in range(1,edges['Flight'][len(edges)-1]):
    idx_flight = np.where(edges['Flight']==i)[0]
    idx_gate  = np.where(edges['Gate']==i)[0]
    thisLHS = LinExpr()
    
    for j in range(0,len(idx_flight)):
        thisLHS += x[i,edges['Flight'][idx_flight[j]]]