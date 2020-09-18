import pandas as pd
import numpy as np
import os
from env import host, user, password

###################### Acquire Telco Churn Data ######################

def new_telco_data():
    '''
    This function reads the telco data from the Codeup db into a df,
    writes it to a csv file, and returns the df.
    '''
    sql_query = '''
                select * 
                from customers as c
                join contract_types as ct
                on ct.contract_type_id = c.contract_type_id
                join internet_service_types as i_s
                on i_s.internet_service_type_id = c.internet_service_type_id
                join payment_types as pt
                on pt.payment_type_id = c.payment_type_id;
                '''
    df = pd.read_sql(sql_query, get_connection('telco_churn'))
    df.to_csv('telco_churn.csv')
    return df

def get_telco_data(cached=False):
    '''
    This function reads in iris data from Codeup database if cached == False
    or if cached == True reads in iris df from a csv file, returns df
    '''
    if cached or os.path.isfile('telco_churn.csv') == False:
        df = new_telco_data()
    else:
        df = pd.read_csv('telco_churn.csv', index_col=0)
    return df