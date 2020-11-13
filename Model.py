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
startTimeSetUp = time.time()
model = Model()
# Load data for this instance
edges  = pd.read_excel(os.path.join(cwd,instance_name),sheet_name='new_dataset')
# gate = []
# for i in range(1,n+1):
#     gate.append(i)
# gate *= edges['Flight'][len(edges)-1]
# print(gate)
# gate = np.array(gate)
# gate = gate.reshape(((len(edges)-1),1))


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


######### Creating Timeslots ##########

Timeslots = list(range(1, len(edges)))
present_aircraft =[]

for i in range(0, len(edges)):
    Check_dep = list(map(int,edges['arr_time'][i]<edges['dep_time']))
    Check_arr = list(map(int,edges['arr_time'][i]>=edges['arr_time']))
    Check_timeslot = np.array(Check_arr)*np.array(Check_dep)
    present_aircraft.append(Check_timeslot)



########### Creating Flight Constraints ################

for i in range(1,edges['Flight'][len(edges)-1]+1): #Looping over all flights
    idx_flight = np.where(edges['Flight']==i)[0] 
    # print(idx_flight)
    flightLHS = LinExpr()
    for j in range(0,len(idx_flight)):
        b = edges['Gate_com'][idx_flight[j]]
        #print(idx_flight[j])
        #print(edges['Flight'][idx_flight[j]])
        flightLHS += b*x[i,edges['Gate'][idx_flight[j]]]  #x11 + x12 + x13 + x14 ... + x43 + x44 i=flight, j=gate      
        
    #print(flightLHS)
    model.addConstr(lhs=flightLHS, sense=GRB.EQUAL, rhs=1, name='Flight_'+str(i))
    
    
    
    

########### Creating Gate Constraints ################

for k in range(1,len(Timeslots)):    #Looping over timeslots
    #idx_timeslot = np.where(edges['Timeslot']==k)[0]
    #print(idx_timeslot)
    for i in range(1,edges['Gate'][len(edges)-1]+1): #Looping over all gates
        idx_gate  = np.where(edges['Gate']==i)[0]
        

        #print(idx_gate)
        gateLHS = LinExpr()
        for j in range(0,len(idx_gate)):
            #a = edges['a_it'][idx_gate[j]]
            a = present_aircraft[k][idx_gate[j]]
            b = edges['Gate_com'][idx_gate[j]]
            gateLHS += a * b * x[edges['Flight'][idx_gate[j]],i]   #x11 + x21 + x31 + x41 ... + x34 + x44 i=flight, j=gate
            #print(edges['a_it'][idx_gate[j]])
        model.addConstr(lhs=gateLHS, sense=GRB.LESS_EQUAL, rhs=1, name='Gate_'+str(i)+'T_'+str(k))
        #print(gateLHS)
            


obj = LinExpr() 
for i in range(0,len(x)):
    obj += edges['Cost'][i]*x[edges['Flight'][i],edges['Gate'][i]]


model.update()
model.setObjective(obj,GRB.MINIMIZE)
model.update()
model.write('model_formulation.lp')    

model.optimize()
endTime   = time.time()

        
      