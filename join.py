# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 17:51:35 2017

@author: Asif
"""

# The script MUST contain a function named azureml_main
# which is the entry point for this module.

# imports up here can be used to 
import pandas as pd


def joinOriginAndDestination(FlightDelaysData , AirportCodesDataset):
    # join on 	OriginAirportID	,airport_id
    df=pd.merge(FlightDelaysData, AirportCodesDataset, how = 'left',left_on ='OriginAirportID',right_on ='airport_id')
    df=df.drop(['airport_id'],axis=1)
    df=df.rename(columns={'city': 'origin_city', 'state': 'origin_state','name':'origin_name'})
    # join on 	OriginAirportID	,DestAirportID
    df_destination=pd.merge(df, AirportCodesDataset, how = 'left',left_on ='DestAirportID',right_on ='airport_id')
    df_destination=df_destination.drop(['airport_id'],axis=1)
    df_final=df_destination.rename(columns={'city': 'dest_city', 'state': 'dest_state','name':'dest_name'})
    #print number of times eacd reposts appeae
    print(df_final.groupby(['dest_name']).size())
    # most frequently appeared
    print(df_final.groupby(['dest_name']).size().nlargest(1))
    return df_final

def azureml_main(FlightDelaysData, AirportCodesDataset):

    # Execution logic goes here
    #print('Input pandas.DataFrame #1:\r\n\r\n{0}'.format(dataframe1))
    return joinOriginAndDestination(FlightDelaysData , AirportCodesDataset)

    

    
    
