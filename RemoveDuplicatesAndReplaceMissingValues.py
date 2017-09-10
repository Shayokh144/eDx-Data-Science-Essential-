# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 13:29:02 2017

@author: Asif
"""
import pandas as pd

def RmvDuplicates(df):
    df=df.drop_duplicates(subset=['Year', 'Month','DayofMonth','Carrier','OriginAirportID','DestAirportID','CRSDepTime','CRSArrTime'], keep='first')
    return df
def ReplaceMissing(df):
    df['DepDelay']=df['DepDelay'].fillna(0) # replace with zero
    df['ArrDelay']=df['ArrDelay'].fillna(0) # replace with zero
    return df
    
def azureml_main(dataframe ):

    dfrmv=RmvDuplicates(dataframe)
    dfrpm=ReplaceMissing(dfrmv)
    return dfrpm
