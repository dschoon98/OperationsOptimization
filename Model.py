# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 10:47:50 2020

@author: Mitchel
"""


# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 22:22:35 2020

@author: abombelli
"""

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

###################
### MODEL SETUP ###
###################

# Keep track of start time to compute overall comptuational performance
startTimeSetUp = time.time()
# Initialize empty model
model = Model()