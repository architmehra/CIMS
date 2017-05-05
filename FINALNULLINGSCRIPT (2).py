# -*- coding: utf-8 -*-
"""
Created on Tue Mar 07 14:32:27 2017

@author: mbdxkame
"""
#script to convert cims data with gaps in time series to a continuous time series 
#with nulls in place of empty time series, for 1 minute data 
#input should be a csv file with igor time already converted to python time by Abs(2082844800-Igortime)

import pandas as pd
import numpy as np
import datetime

cims_df = pd.read_csv('C:\Users\mbdxkame\Documents\Beijing\minuteaverageddatamarch17\HONO\cimshono.csv')

pythontime = cims_df['pythontime'] #defined excel column names to variables 
cimshono = cims_df['cimshono']
#hydrogenperoxide = cims_df['Hydrogenperoxide']
#methylisocyanate = cims_df['methylisocyanate']
#ethylnitrate = cims_df['ethylnitrate']
#malonicacid = cims_df['malonicacid']
#levoglucosan = cims_df['levoglucosan']
#pinicacid = cims_df['pinicacid']
#norpinicacid = cims_df['norpinicacid']

#print formic_df

time2 = []

time2 = cims_df['pythontime'].values.tolist()

#print time2 

time3 = []

for all in time2: 
    time3.append(datetime.datetime.fromtimestamp(all).strftime("%d-%m-%y %H:%M:%S"))

#print time3
time4 = []

for all in time3: 
    time4.append(datetime.datetime.strptime(all,"%d-%m-%y %H:%M:%S"))

#time4 is in datetime format 

#print time4

table_df = pd.DataFrame(
    {'cimshono': cimshono,
     'time4': time4,
    })
#output table can be used for adding nulls (time column is time4)

table_df['time4'] = table_df['time4'].values.astype('datetime64[m]')

indexed_df = table_df.set_index(table_df['time4'])

df2 = pd.DataFrame(data=None, index=pd.date_range(freq='1Min', start=indexed_df.index.min(), end=indexed_df.index.max()))

df2['value']=np.NaN
   
#print df2

df3 = df2.combine_first(indexed_df)
             
#print df3

df3.to_csv('C:\Users\mbdxkame\Documents\Beijing\minuteaverageddatamarch17\HONO\cimshononulled.csv')

print "complete"

