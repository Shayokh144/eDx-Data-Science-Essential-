# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 13:29:02 2017

@author: Asif
"""

# The script MUST contain a function named azureml_main
# which is the entry point for this module.

# imports up here can be used to 
import pandas as pd

# The entry point function can contain up to two input arguments:
#   Param<dataframe1>: a pandas.DataFrame
#   Param<dataframe2>: a pandas.DataFrame

def RmvDuplicates(df):
    df=df.drop_duplicates(subset=['Year', 'Month','DayofMonth','Carrier','OriginAirportID','DestAirportID','CRSDepTime','CRSArrTime'], keep='first')
    return df
def ReplaceMissing(df):
    df['DepDelay']=df['DepDelay'].fillna(0)
    df['ArrDelay']=df['ArrDelay'].fillna(0)
    return df
    
def azureml_main(dataframe ):

    # Execution logic goes here
    #print('Input pandas.DataFrame #1:\r\n\r\n{0}'.format(dataframe1))

    # If a zip file is connected to the third input port is connected,
    # it is unzipped under ".\Script Bundle". This directory is added
    # to sys.path. Therefore, if your zip file contains a Python file
    # mymodule.py you can import it using:
    # import mymodule
    
    # Return value must be of a sequence of pandas.DataFrame
    dfrmv=RmvDuplicates(dataframe)
    dfrpm=ReplaceMissing(dfrmv)
    return dfrpm
