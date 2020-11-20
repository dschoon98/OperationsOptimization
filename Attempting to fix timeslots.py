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

    #Trying to write timeslot stuff     
appie = []
beppie = []
arr_times = []
dep_times = []
# for t in range(0,1440):
#     if t
############## DONT FORGET TO CHANGE n BELOW ######################
n = 4   # NUMBER OF GATES, SHOULD BE CONSTANT


pipo  = pd.read_excel(os.path.join(cwd,instance_name),sheet_name='Blad3')

########## Arrival times #############
for i in pipo['arr_time']:
    a = str(i)
    minutes = int(a[3])*10+int(a[4]) # = e.g. 15 in 09:15
    hours = int(a[0])*10+int(a[1])   # = e.g. 9 in 09:15
    appie.append(hours*60+minutes)
for index, element in enumerate(appie):
	if index % n == 0:
		arr_times.append(element)

########## Departure times #############
for i in pipo['dep_time']:
    a = str(i)
    minutes = int(a[3])*10+int(a[4]) # = e.g. 15 in 09:15
    hours = int(a[0])*10+int(a[1])   # = e.g. 9 in 09:15
    beppie.append(hours*60+minutes)
for index, element in enumerate(beppie):
	if index % n == 0:
		dep_times.append(element)
gate = []
for i in range(1,n+1):
    gate.append(i)
gate *= pipo['Flight'][len(pipo)-1]
print(gate)
gate = np.array(gate)
gate = gate.reshape(((len(pipo)),1))



startTimeSetUp = time.time()
model = Model()

#################
### VARIABLES ###
#################
x = {}
for i in range(0,len(pipo)):
    x[pipo['Flight'][i],pipo['Gate'][i]]=model.addVar(lb=0, ub=1, vtype=GRB.BINARY,name="x%s%s"%(pipo['Flight'][i],pipo['Gate'][i]))

            
model.update()

###################
### CONSTRAINTS ###
###################

for i in range(1,pipo['Flight'][len(pipo)-1]+1): #Looping over all flights
    idx_flight = np.where(pipo['Flight']==i)[0]
    # print(idx_flight)
    flightLHS = LinExpr()
    for j in range(0,len(idx_flight)):
        b = pipo['Gate_com'][idx_flight[j]]
        #print(idx_flight[j])
        #print(pipo['Flight'][idx_flight[j]])
        flightLHS += x[i,pipo['Gate'][idx_flight[j]]]  #x11 + x12 + x13 + x14 ... + x43 + x44 i=flight, j=gate      
        
    #print(flightLHS)
    model.addConstr(lhs=flightLHS, sense=GRB.EQUAL, rhs=1, name='Flight_'+str(i))
    
# Load data for this instance
    
# #Trying to write timeslot stuff     
# pipo  = pd.read_excel(os.path.join(cwd,instance_name),sheet_name='Blad3')
# for i in pipo['arr_time']:
#     a = str(i)
#     minutes = int(a[3])*10+int(a[4]) # = e.g. 15 in 09:15
#     hours = int(a[0])*10+int(a[1])   # = e.g. 9 in 09:15
#     print(minutes)
#     print(hours)
    





for i in range(1,pipo['Gate'][len(pipo)-1]+1): #Looping over all gates
    idx_gate  = np.where(pipo['Gate']==i)
    

    #print(idx_gate)
    gateLHS = LinExpr()
    for j in range(0,len(idx_gate)):
        #if 
        b = pipo['Gate_com'][idx_gate[j]]
        gateLHS += b * x[pipo['Flight'][idx_gate[j]],i]   #x11 + x21 + x31 + x41 ... + x34 + x44 i=flight, j=gate
        #print(pipo['a_it'][idx_gate[j]])
    model.addConstr(lhs=gateLHS, sense=GRB.LESS_EQUAL, rhs=1, name='Gate_'+str(i))
    #print(gateLHS)
        


obj        = LinExpr() 
for i in range(0,len(x)):
    obj += pipo['Cost'][i]*x[pipo['Flight'][i],pipo['Gate'][i]]


model.update()
model.setObjective(obj,GRB.MINIMIZE)
model.update()
model.write('model_formulation.lp')    

model.optimize()
endTime   = time.time()
        