#fhajkgibfdjan
# Loading packages that are used in the code

import numpy as np
import os
import pandas as pd
import time
from gurobipy import Model,GRB,LinExpr
import pickle
from copy import deepcopy
import datetime

# Get path to current folder
cwd = os.getcwd()

# Get all instances
full_list           = os.listdir(cwd)

# instance name
instance_name = 'dataset.xlsx'
startTimeSetUp = time.time()
model = Model()

# Load data for this instance
edges  = pd.read_excel(os.path.join(cwd,instance_name),sheet_name='Flights')
gate_data = pd.read_excel(os.path.join(cwd,instance_name),sheet_name='Gates')

#################
### VARIABLES ###
#################


n_gates = len(gate_data['Gates']) #number of gates
buffer_time = 0 #min


x = {}
for i in range(len(edges)):
    for j in range(n_gates):
        x[i+1,j+1]=model.addVar(lb=0, ub=1, vtype=GRB.BINARY,name="x%s%s"%(i+1,j+1))
        
t = {}        
for i in range(1, len(edges)+1):
    for j in range(1, n_gates+1):
        for i_p in range(1, len(edges)+1):
            for j_p in range(1, n_gates+1):
                t[i,j,i_p,j_p] = model.addVar(lb=0, ub=1, vtype=GRB.BINARY,name="t%s%s%s%s"%(i,j,i_p,j_p))

g = {} 
for j in range(n_gates):
    g[j+1] = model.addVar(lb=0, ub=1, vtype=GRB.BINARY,name="g%s"%(j+1))    
            
model.update()

###################
### CONSTRAINTS ###
###################


######### Creating Timeslots ##########

Timeslots = list(range(1, len(edges)))
present_aircraft =[]
arr_time = edges['arr_time']
dep_time = edges['dep_time']


## Buffer time ##
for i in range(len(edges)):
    arr = arr_time[i]
    if arr.minute-buffer_time < 0:
        arr = arr.replace(arr.hour -1, arr.minute-buffer_time+60)
    else:
        arr = arr.replace(arr.hour, arr.minute-buffer_time)
    arr_time[i] = arr
    
    dep = dep_time[i]
    if dep.minute+buffer_time > 59:
        dep = dep.replace(dep.hour +1, dep.minute+buffer_time-60)
    else:
        dep = dep.replace(dep.hour, dep.minute+buffer_time)
    dep_time[i] = dep


for i in range(0, len(edges)):
    Check_dep = list(map(int,arr_time[i]<dep_time))
    Check_arr = list(map(int,arr_time[i]>=arr_time))
    Check_timeslot = np.array(Check_arr)*np.array(Check_dep)
    present_aircraft.append(Check_timeslot)
    
    
    
########## Creating Gate Compatability and Cost Matrix ##############

gate_comp = np.zeros((len(edges), n_gates))
distance = np.zeros((len(edges), n_gates))

for i in range(0, len(edges)):
    for j in range(0, n_gates):
        distance[i][j] = edges["Gate %s"%(j+1)][i]
        if edges["Gate %s"%(j+1)][i] != 0:
            gate_comp[i][j] = 1
            
 ##############  Creating transfer matrix    #####################       
        
Transfers = np.zeros((len(edges), len(edges)))
for i in range(len(edges)):
    for j in range(len(edges)):
        Transfers[i][j] = edges["Flight %s"%(j+1)][i]

########### Creating Flight Constraints #########################

for i in range(len(edges)):
    flightLHS = LinExpr()
    for j in range(n_gates):
        flightLHS += gate_comp[i][j]*x[i+1,j+1]
    model.addConstr(lhs=flightLHS, sense=GRB.EQUAL, rhs=1, name='Flight_'+str(i+1))

    
    

########### Creating Gate Constraints ################

for k in range(len(present_aircraft)):
    for j in range(n_gates):
        gateLHS = LinExpr()
        for i in range(len(edges)):
            gateLHS += gate_comp[i][j]*present_aircraft[k][i]*x[i+1, j+1]
        model.addConstr(lhs=gateLHS, sense=GRB.LESS_EQUAL, rhs=1, name='Gate_'+str(j+1)+'T_'+str(k+1))
        
        
########### Creating Transfer Contraints ##############
 
for i in range(1, len(edges)+1):
    for j in range(1, n_gates+1):
        for i_p in range(1, len(edges)+1):
            for j_p in range(1, n_gates+1):
                transLHS = LinExpr()
                transLHS = x[i,j] + x[i_p,j_p] - t[i,j,i_p,j_p]
                model.addConstr(lhs=transLHS, sense=GRB.LESS_EQUAL, rhs=1, name='Trans_'+str(i)+str(j)+str(i_p)+str(j_p))
           
########### Minimizing number of gates used #####################
for j in range(n_gates):
    mingateLHS = LinExpr()
    for i in range(len(edges)):
        mingateLHS += x[i+1,j+1]
    mingateLHS += -n_gates*g[j+1]
    model.addConstr(lhs=mingateLHS, sense=GRB.LESS_EQUAL, rhs=0, name='GateUsed_'+str(j+1))


        
########## Objective Function ###################

obj = LinExpr() 
for i in range(1, len(edges)+1):
    for j in range(1, n_gates+1):
        #obj += distance[i-1][j-1]*edges["Passengers"][i-1]*x[i, j]
        for i_p in range(1, len(edges)+1):
            for j_p in range(1, n_gates+1):
                 obj += Transfers[i-1][i_p-1] * (max(distance[:,j-1]) + max(distance[:,j_p-1])) * t[i,j,i_p,j_p]


model.update()
model.setObjective(obj,GRB.MINIMIZE)
model.update()
model.write('model_formulation.lp')    

model.optimize()
endTime   = time.time()

        
      