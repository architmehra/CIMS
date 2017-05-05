# -*- coding: utf-8 -*-
"""
Created on Sat Mar 04 01:02:23 2017

@author: mbdxkame
"""

import pandas as pd

beijing_df = pd.read_csv('C:\Users\mbdxkame\Documents\Beijing\minuteaverageddatamarch17\FIGAERO\\nitric.csv') 

#need to change the name of the import file each time

localtime = beijing_df ['localtime'] #defined excel column names to variables 
nitric = beijing_df['nitric']
eyeon = beijing_df['eyeon']
#HCN = beijing_df['HCN']
#formic = beijing_df['formic']
#nitric = beijing_df['nitric']
#CO = beijing_df['CO']
#windspeed = beijing_df['windspeed']
#WD = beijing_df ['WD']

 #winddirection 
 #defined excel column names to variables 

#define column of whatever else I want to plot over same time series 
#according to NOx, can also make extra columns, the quote marks need to be column name


#print beijing_df[beijing_df.nox_av >100]  #change nox value here to test 

#can put a different value that isn't nox here to test according to a different parameter
#can also put == or != as tests

beijing_df[(beijing_df.eyeon ==2) | (beijing_df.eyeon==3) | (beijing_df.eyeon ==4)].to_csv('C:\Users\mbdxkame\Documents\Beijing\minuteaverageddatamarch17\FIGAERO\\thermogram.csv')
#print beijing_df[((beijing_df.eyeon < 90.0) & (beijing_df.WD > 270))]


#df.query('foo == 222 | bar == 444')

#beijing_df[((beijing_df.WD < 90.0) & (beijing_df.WD > 270))].to_csv('C:\Users\mbdxkame\Documents\Beijing\minuteaverageddatamarch17\Processing9317\windfromnorth.csv')
print "complete" 

#brackets are very important for wind direction
#remember to change this nox value to print 
#created a csv for a if nox is greater than 200 
#need to change the name of the export file each time



