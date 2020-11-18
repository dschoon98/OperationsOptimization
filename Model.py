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
n_towes = 2  # amount of times a flight can be towed
buffer_time = 0 #min


x = {}   # x_{i,j,k,l} = variable for each {flight==i, gate it is currently at==j, amount of times it can be towed==k, amount of times it has been towed==l}
y = {}   # towing variables y_{i,k}
for i in range(1,len(edges)+1):
    for k in range(n_towes +1):
        y[i,k] = model.addVar(lb=0, ub=1, vtype=GRB.BINARY, name="y%s%s"%(i,k))
    for j in range(1,n_gates+1):
        for k in range(n_towes +1):
            for l in range(k+1):
                x[i,j,k,l]=model.addVar(lb=0, ub=1, vtype=GRB.BINARY,name="x%s%s%s%s"%(i,j,k,l))
        
t = {}        # = t_{i,j,i',j'} = transfer between flight i at gate j to flight i' at gate j'
for i in range(1, len(edges)+1):
    for j in range(1, n_gates+1):
        for i_p in range(1, len(edges)+1):
            for j_p in range(1, n_gates+1):
                t[i,j,i_p,j_p] = model.addVar(lb=0, ub=1, vtype=GRB.BINARY,name="t%s%s%s%s"%(i,j,i_p,j_p))

g = {}   #Here we make variables for 
for j in range(1,n_gates+1):
    g[j] = model.addVar(lb=0, ub=1, vtype=GRB.BINARY,name="g%s"%(j))  


    
 
            
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

###### Making a time-slot for each time an aircraft arrives and departs ####
for i in range(0, len(edges)):
    Check_dep = list(map(int,arr_time[i]<dep_time))
    Check_arr = list(map(int,arr_time[i]>=arr_time))
    Check_timeslot = np.array(Check_arr)*np.array(Check_dep)  
    present_aircraft.append(Check_timeslot)
    
for i in range(0, len(edges)):
    Check_dep2 = list(map(int,dep_time[i]>=arr_time))
    Check_arr2 = list(map(int,dep_time[i]<dep_time))
    Check_timeslot2 = np.array(Check_arr2)*np.array(Check_dep2)
    present_aircraft.append(Check_timeslot2)
    
########## Creating Gate Compatability and Distance Matrix ##############

gate_comp = np.zeros((len(edges), n_gates))   #Making dummy array for gate compatibility values
distance = np.zeros((len(edges), n_gates))     #Making dummy array for distance values

for i in range(1, len(edges)+1):
    for j in range(1, n_gates+1):
        distance[i-1][j-1] = edges["Gate %s"%(j)][i-1] #distance is defined as the distance from a certain gate to the terminal
        if edges["Gate %s"%(j)][i-1] != 0:
            gate_comp[i-1][j-1] = 1
            
##############  Creating transfer matrix    #####################       
        
Transfers = np.zeros((len(edges), len(edges)))  #Making dummy array for transfer matrix
for i in range(1,len(edges)+1):
    for j in range(1,len(edges)+1):
        Transfers[i-1][j-1] = edges["Flight %s"%(j)][i-1]

########## Towing constraint ##########
for i in range(1, len(edges)+1):
    towLHS = LinExpr()
    for k in range(n_towes +1):
        towLHS += y[i,k]
    model.addConstr(lhs=towLHS, sense=GRB.EQUAL, rhs=1, name='Tow_'+str(i))


########### Creating Flight Constraints #########################

for i in range(1, len(edges)+1):
    for k in range(n_towes+1):
        for l in range(k+1):
            flightLHS = LinExpr()
            for j in range(1, n_gates+1):
                flightLHS += gate_comp[i-1][j-1]*x[i,j,k,l]

            flightLHS += - y[i,k]        
            model.addConstr(lhs=flightLHS, sense=GRB.EQUAL, rhs=0, name='Flight_'+str(i)+"_Tow"+str(k)+str(l))

    
    

########### Creating Gate Constraints ################


# for s in range(1,len(present_aircraft)+1):
#     for j in range(1,n_gates+1):
#         for k in range(n_towes+1):
#             for l in range(k+1):
#                 gateLHS = LinExpr()
#                 for i in range(1,len(edges)+1):
#                     gateLHS += gate_comp[i-1][j-1]*present_aircraft[s-1][i-1]*x[i,j,k,l]
#                 model.addConstr(lhs=gateLHS, sense=GRB.LESS_EQUAL, rhs=1, name='Gate_'+str(j)+"Tow"+str(k)+str(l)+'T'+str(s))
        
for s in range(1,len(present_aircraft)+1):
    
    for j in range(1,n_gates+1):
        gateLHS = LinExpr()
        for i in range(1,len(edges)+1):
            for k in range(n_towes+1):
                for l in range(k+1):
                    if i==s:
                        l==0 
                        
                    gateLHS += gate_comp[i-1][j-1]*present_aircraft[s-1][i-1]*x[i,j,k,l]
        model.addConstr(lhs=gateLHS, sense=GRB.LESS_EQUAL, rhs=1, name='Gate_'+str(j)+'T'+str(s))

# ########### Creating Transfer Contraints ##############
 
for i in range(1, len(edges)+1):
    for j in range(1, n_gates+1):
        for k in range(n_towes+1):
            for l in range(k+1):
                for k_p in range(n_towes+1):
                    for l_p in range(k_p+1):
                        for i_p in range(1, len(edges)+1):
                            for j_p in range(1, n_gates+1):
                                transLHS = LinExpr()
                                transLHS = x[i,j,k,l] + x[i_p,j_p,k_p,l_p] - t[i,j,i_p,j_p]
                                model.addConstr(lhs=transLHS, sense=GRB.LESS_EQUAL, rhs=1, name='Trans_'+str(i)+str(j)+str(i_p)+str(j_p))
                           

# ########### Minimizing number of gates used #####################
for j in range(1,n_gates+1):
    mingateLHS = LinExpr()
    for i in range(1,len(edges)+1):
        for k in range(n_towes+1):
            for l in range(k+1):
                mingateLHS += x[i,j,k,l]
    mingateLHS += -n_gates*10*g[j]
    model.addConstr(lhs=mingateLHS, sense=GRB.LESS_EQUAL, rhs=0, name='GateUsed_'+str(j))
        

        
# ########## Objective Function ###################


obj = LinExpr() 
for i in range(1,len(edges)+1):
    for k in range(n_towes+1):
        towing_cost = edges["Tow %s"%(k)][i-1]        
        obj += towing_cost*y[i,k]
for j in range(1, n_gates+1):
    #obj += gate_data['gate_cost'][j-1] * g[j]
    for i in range(1, len(edges)+1):
        for k in range(n_towes+1):
            for l in range(k+1):
                towing_cost = edges["Tow %s"%(k)][i-1]
                if j==6 and not(k==2 and l==1):    #Prevents arriving or departing at storage gate
                    obj += x[i,j,k,l]*1000000 
                if k == 0:
                    added_gate_cost = 3
                else:
                    if l==0:
                        added_gate_cost = 1
                    else:
                        added_gate_cost = 2
                        if k==2 and l==1:
                            added_gate_cost = 0
                        
                obj += distance[i-1][j-1]*added_gate_cost*edges["Passengers"][i-1]*x[i, j,k,l] #minimize total walking distance * passengers
        # for i_p in range(1, len(edges)+1):
        #     for j_p in range(1, n_gates+1):
        #           #minimize transfer distance
        #           obj += Transfers[i-1][i_p-1] * (max(distance[:,j-1]) + max(distance[:,j_p-1])) * t[i,j,i_p,j_p]  #minimize transfer distance * passengers

model.update()
model.setObjective(obj,GRB.MINIMIZE)
model.update()
model.write('model_formulation.lp')    

model.optimize()
endTime   = time.time()
      