# -*- coding: utf-8 -*-
"""
Created on Wed Mar 08 10:38:11 2017

@author: mbdxkame
"""

#code for converting igor time to real time

import datetime

# value from igor is: 3562368437
#value to convert is : -2082844800

# it is actually that value minus igor time 

print abs(2082844800 - 3562368437) 

print datetime.datetime.fromtimestamp(1479523637).strftime("%d-%m-%y %H:%M:%S")