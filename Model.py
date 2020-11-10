#fhajkgibfdjan
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
edges  = pd.read_excel(os.path.join(cwd,instance_name),sheet_name='Blad1')

startTimeSetUp = time.time()
model = Model()

#################
### VARIABLES ###
#################
x = {}
for i in range(0,len(edges)):
    x[edges['Flight'][i],edges['Gate'][i]]=model.addVar(lb=0, ub=1, vtype=GRB.BINARY,name="x%s%s"%(edges['Flight'][i],edges['Gate'][i]))

            
model.update()

###################
### CONSTRAINTS ###
###################

for i in range(1,edges['Flight'][len(edges)-1]+1): #Looping over all flights
    idx_flight = np.where((edges['Flight']==i) & (edges['Timeslot']==1))[0]
    # print(idx_flight)
    idx_compat = npwhere.
    flightLHS = LinExpr()
      
    for j in range(0,len(idx_flight)):
        #print(idx_flight[j])
        #print(edges['Flight'][idx_flight[j]])
        flightLHS += x[i,edges['Gate'][idx_flight[j]]]  #x11 + x12 + x13 + x14 ... + x43 + x44 i=flight, j=gate      
        
    #print(flightLHS)
    model.addConstr(lhs=flightLHS, sense=GRB.EQUAL, rhs=1, name='Flight_'+str(i))
    

for k in range(1,edges['Timeslot'][len(edges)-1]+1):    
    idx_timeslot = np.where(edges['Timeslot']==k)[0]
    #print(idx_timeslot)

    for i in range(1,edges['Gate'][len(edges)-1]+1): #Looping over all gates
        idx_gate  = np.where((edges['Gate']==i) & (edges['Timeslot']==k))[0]
        #print(idx_gate)
        gateLHS = LinExpr()
        for j in range(0,len(idx_gate)):
            a = edges['a_it'][idx_gate[j]]

            gateLHS += a*x[edges['Flight'][idx_gate[j]],i]   #x11 + x21 + x31 + x41 ... + x34 + x44 i=flight, j=gate
            #print(edges['a_it'][idx_gate[j]])
        model.addConstr(lhs=gateLHS, sense=GRB.LESS_EQUAL, rhs=1, name='Gate_'+str(i)+'T_'+str(k))
        #print(gateLHS)
            

b = edges['Gate_compatibility'][]
obj        = LinExpr() 

for i in range(0,len(edges)):
    obj += edges['Cost'][i]*x[edges['Flight'][i],edges['Gate'][i]]


model.update()
model.setObjective(obj,GRB.MINIMIZE)
model.update()
model.write('model_formulation.lp')    

model.optimize()
endTime   = time.time()

        
        
    #     for i in range(1,edges['Flight'][len(edges)-1]):
    # idx_flight = np.where(edges['Flight']==i)[0]
    # idx_gate  = np.where(edges['Gate']==i)[0]
    # thisLHS = LinExpr()
        
    
    
    
    # for j in range(0,len(idx_flight)):
    #     thisLHS += x[i,edges['Flight'][idx_flight[j]]]