import pandas as pd
import numpy as np
import scipy as sp 

from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, MinMaxScaler
from sklearn.preprocessing import StandardScaler

###################### Prepare Telco Churn Data ######################

def scale(train, validate, test):
    scaler = MinMaxScaler()
    train[['tenure', 'monthly_charges', 'total_charges','tenure_years']] = scaler.fit_transform(train[['tenure', 'monthly_charges', 'total_charges','tenure_years']])
    validate[['tenure', 'monthly_charges', 'total_charges','tenure_years']] = scaler.transform(validate[['tenure', 'monthly_charges', 'total_charges','tenure_years']])
    test[['tenure', 'monthly_charges', 'total_charges','tenure_years']]= scaler.transform(test[['tenure', 'monthly_charges', 'total_charges','tenure_years']])
    return train, validate, test

def train_valid_test(df):
    train_validate, test = train_test_split(df, test_size = .2, random_state = 123, stratify = df.churn)
    train, validate = train_test_split(train_validate, test_size = .3, random_state = 123, stratify = train_validate.churn)
    return train, validate, test

def prep_telco_data_explore(df):
    # Delete columns contract_type_id, internet_service_type_id, payment_type_id    
    df.drop(columns = ['contract_type_id','internet_service_type_id', 'payment_type_id'], inplace = True)
    # Replace partner, dependents, churn, phone_service, paperless billing, with boolean value
    df.partner.replace(['Yes', 'No'], [1,0], inplace = True)
    df.dependents.replace(['Yes', 'No'], [1,0], inplace = True)
    df.churn.replace(['Yes', 'No'], [1,0], inplace = True)
    df.phone_service.replace(['Yes', 'No'], [1,0], inplace = True)
    df.paperless_billing.replace(['Yes', 'No'], [1,0], inplace = True)
    ## Add dummy variables as new columns in dataframe and rename them, delete origional
    df["gender_cc"] = df["gender"].astype('category')
    df["gender_cc"] = df["gender_cc"].cat.codes
    #gender = df.gender.str.get_dummies()
    #df = pd.concat([df, gender], axis=1)
    df["payment_type_cc"] = df["payment_type"].astype('category')
    df["payment_type_cc"] = df["payment_type_cc"].cat.codes
    #df.rename(columns = {'Female': 'is_female', 'Male': 'is_male'}, inplace = True)
    #df.drop(columns = ['gender'], inplace = True)
    ## Add dummy variables as new columns in dataframe and rename them, delete origional
    #multiple = df.multiple_lines.str.get_dummies()
    df["multiple_lines_cc"] = df["multiple_lines"].astype('category')
    df["multiple_lines_cc"] = df["multiple_lines_cc"].cat.codes
    #df = pd.concat([df, multiple], axis=1)
    #df.rename(columns = {'No': 'no_multiple_lines', 'Yes': 'yes_multiple_lines'}, inplace = True)
    #df.drop(columns = ['multiple_lines'], inplace = True)
    ## Add dummy variables as new columns in dataframe and rename them, delete origional
    #multiple = df.online_security.str.get_dummies()
    df["online_security_cc"] = df["online_security"].astype('category')
    df["online_security_cc"] = df["online_security_cc"].cat.codes
    #df = pd.concat([df, multiple], axis=1)
    #df.rename(columns = {'No': 'no_online_security', 'Yes': 'yes_online_security'}, inplace = True)
    #df.drop(columns = ['online_security'], inplace = True)
    ## Add dummy variables as new columns in dataframe and rename them, delete origional
    #multiple = df.online_backup.str.get_dummies()
    df["online_backup_cc"] = df["online_backup"].astype('category')
    df["online_backup_cc"] = df["online_backup_cc"].cat.codes
    #df = pd.concat([df, multiple], axis=1)
    #df.rename(columns = {'No': 'no_online_backup', 'Yes': 'yes_online_backup'}, inplace = True)
    #df.drop(columns = ['online_backup'], inplace = True)
    ## Add dummy variables as new columns in dataframe and rename them, delete origional
    #multiple = df.device_protection.str.get_dummies()
    df["device_protection_cc"] = df["device_protection"].astype('category')
    df["device_protection_cc"] = df["device_protection_cc"].cat.codes
    #df = pd.concat([df, multiple], axis=1)
    #df.rename(columns = {'No': 'no_device_protection', 'Yes': 'yes_device_protection'}, inplace = True)
    #df.drop(columns = ['device_protection'], inplace = True)
    ## Add dummy variables as new columns in dataframe and rename them, delete origional
    #multiple = df.tech_support.str.get_dummies()
    df["tech_support_cc"] = df["tech_support"].astype('category')
    df["tech_support_cc"] = df["tech_support_cc"].cat.codes
    #df = pd.concat([df, multiple], axis=1)
    #df.rename(columns = {'No': 'no_tech_support', 'Yes': 'yes_tech_support'}, inplace = True)
    #df.drop(columns = ['tech_support'], inplace = True)
    ## Add dummy variables as new columns in dataframe and rename them, delete origional
    #multiple = df.streaming_tv.str.get_dummies()
    df["streaming_tv_cc"] = df["streaming_tv"].astype('category')
    df["streaming_tv_cc"] = df["streaming_tv_cc"].cat.codes
    #df = pd.concat([df, multiple], axis=1)
    #df.rename(columns = {'No': 'no_streaming_tv', 'Yes': 'yes_streaming_tv'}, inplace = True)
    #df.drop(columns = ['streaming_tv', 'No internet service'], inplace = True)
    #df.drop(columns = ['No internet service'], inplace = True)
    ## Add dummy variables as new columns in dataframe and rename them, delete origional
    #multiple = df.streaming_movies.str.get_dummies()
    df["streaming_movies_cc"] = df["streaming_movies"].astype('category')
    df["streaming_movies_cc"] = df["streaming_movies_cc"].cat.codes
    #df = pd.concat([df, multiple], axis=1)
    #df.rename(columns = {'No': 'no_streaming_movies', 'Yes': 'yes_streaming_movies'}, inplace = True)
    #df.drop(columns = ['streaming_movies'], inplace = True)
    # Add dummy variables as new columns in dataframe and rename them, delete origional
    df["contract_type_cc"] = df["contract_type"].astype('category')
    df["contract_type_cc"] = df["contract_type_cc"].cat.codes
    #multiple = df.contract_type.str.get_dummies()
    #df = pd.concat([df, multiple], axis=1)
    #df.rename(columns = {'Month-to-month': 'month_to_month_contract', 'One year': 'one_year_contract', 'Two year': 'two_year_contract'}, inplace = True)
    #df.drop(columns = ['contract_type'], inplace = True)
    ## Add dummy variables as new columns in dataframe and rename them, delete origional
    multiple = df.payment_type.str.get_dummies()
    df = pd.concat([df, multiple], axis=1)
    df.rename(columns = {'Bank transfer (automatic)': 'bank_transfer_auto', 'Credit card (automatic)': 'credit_card_auto', 'Electronic check': 'e_check', 'Mailed check': 'mail_check'}, inplace = True)
    #multiple = df.internet_service_type.str.get_dummies()
    #df = pd.concat([df, multiple], axis=1)
    #df.rename(columns = {'DSL': 'dsl', 'Fiber optic': 'fiber_optic'}, inplace = True)
    # Internet Service Type
    multiple = df.contract_type.str.get_dummies()
    df = pd.concat([df, multiple], axis=1)
    df.rename(columns = {'Month-to-month': 'month_to_month_contract', 'One year': 'one_year_contract', 'Two year': 'two_year_contract'}, inplace = True)
    #
    df["internet_service_type_cc"] = df["internet_service_type"].astype('category')
    df["internet_service_type_cc"] = df["internet_service_type_cc"].cat.codes
    # Internet serivce
    df['internet_service'] = df.internet_service_type != 'None'
    result = df['internet_service'].astype(int)
    df['internet_service'] = result
    # Dummies
    multiple = df.internet_service_type.str.get_dummies()
    df = pd.concat([df, multiple], axis=1)
    df.rename(columns = {'DSL': 'dsl', 'Fiber optic': 'fiber_optic'}, inplace = True)
    #df.drop(columns = ['internet_service_type','None'], inplace = True)
    ## Add dummy variables as new columns in dataframe and rename them, delete origional
    #multiple = df.payment_type.str.get_dummies()
    #df = pd.concat([df, multiple], axis=1)
    #df.rename(columns = {'Bank transfer (automatic)': 'auto_bank_transfer', 'Credit card (automatic)': 'auto_credit_card', 'Electronic check': 'e_check', 'Mailed check': 'mail_check'}, inplace = True)
    #df.drop(columns = ['payment_type'], inplace = True)
    # Change total_charges to float from object
    df['total_charges'] = pd.to_numeric(df['total_charges'],errors='coerce')
    # Add feature of tenure in terms of years
    df['tenure_years'] = round(df.tenure / 12, 2)
    #
    df["total_charges"].fillna(0, inplace = True) 
    #split data
    # train, validate, test = train_valid_test(df)
    # train, validate, test = scale(train, validate, test)
    return df

def prep_telco_data_model(df):
    # Delete redundent columns contract_type_id, internet_service_type_id, payment_type_id    
    df.drop(columns = ['contract_type_id','internet_service_type_id', 'payment_type_id'], inplace = True)
    # Replace partner, dependents, churn, phone_service, paperless billing, with boolean value
    df.partner.replace(['Yes', 'No'], [1,0], inplace = True)
    df.dependents.replace(['Yes', 'No'], [1,0], inplace = True)
    df.churn.replace(['Yes', 'No'], [1,0], inplace = True)
    df.phone_service.replace(['Yes', 'No'], [1,0], inplace = True)
    df.paperless_billing.replace(['Yes', 'No'], [1,0], inplace = True)
    ## Change gender to categorical category codes and drop origional
    df["gender_cc"] = df["gender"].astype('category')
    df["gender_cc"] = df["gender_cc"].cat.codes
    df.drop(columns = ['gender'], inplace = True)
    # ## Change payment_type to categorical category codes and drop origional
    df["payment_type_cc"] = df["payment_type"].astype('category')
    df["payment_type_cc"] = df["payment_type_cc"].cat.codes
    ## Change multiple lines to categorical category codes and drop origional
    df["multiple_lines_cc"] = df["multiple_lines"].astype('category')
    df["multiple_lines_cc"] = df["multiple_lines_cc"].cat.codes
    df.drop(columns = ['multiple_lines'], inplace = True)
    ## Change online_security to categorical category codes and drop origional
    df["online_security_cc"] = df["online_security"].astype('category')
    df["online_security_cc"] = df["online_security_cc"].cat.codes
    df.drop(columns = ['online_security'], inplace = True)
    ## Change online_backup to categorical category codes and drop origional
    df["online_backup_cc"] = df["online_backup"].astype('category')
    df["online_backup_cc"] = df["online_backup_cc"].cat.codes
    df.drop(columns = ['online_backup'], inplace = True)
    ## Change device_portection to categorical category codes and drop origional
    df["device_protection_cc"] = df["device_protection"].astype('category')
    df["device_protection_cc"] = df["device_protection_cc"].cat.codes
    df.drop(columns = ['device_protection'], inplace = True)
    ## Change tech_support to categorical category codes and drop origional
    df["tech_support_cc"] = df["tech_support"].astype('category')
    df["tech_support_cc"] = df["tech_support_cc"].cat.codes
    df.drop(columns = ['tech_support'], inplace = True)
    ## Change streaming_tv to categorical category codes and drop origional
    df["streaming_tv_cc"] = df["streaming_tv"].astype('category')
    df["streaming_tv_cc"] = df["streaming_tv_cc"].cat.codes
    df.drop(columns = ['streaming_tv'], inplace = True)
    ## Change streaming_movies to categorical category codes and drop origional
    df["streaming_movies_cc"] = df["streaming_movies"].astype('category')
    df["streaming_movies_cc"] = df["streaming_movies_cc"].cat.codes
    df.drop(columns = ['streaming_movies'], inplace = True)
    # Create dummy variables of payment type and drop origional
    multiple = df.payment_type.str.get_dummies()
    df = pd.concat([df, multiple], axis=1)
    df.rename(columns = {'Bank transfer (automatic)': 'bank_transfer_auto', 'Credit card (automatic)': 'credit_card_auto', 'Electronic check': 'e_check', 'Mailed check': 'mail_check'}, inplace = True)
    df.drop(columns = ['payment_type'], inplace = True)
    # Create dummy variables of contract type and drop origional
    multiple = df.contract_type.str.get_dummies()
    df = pd.concat([df, multiple], axis=1)
    df.rename(columns = {'Month-to-month': 'month_to_month_contract', 'One year': 'one_year_contract', 'Two year': 'two_year_contract'}, inplace = True)
    df.drop(columns = ['contract_type'], inplace = True)
    # Add new categorcial variable internet_service
    df['internet_service'] = df.internet_service_type != 'None'
    result = df['internet_service'].astype(int)
    df['internet_service'] = result
    ## Add dummy variables of internet service and drop origional
    multiple = df.internet_service_type.str.get_dummies()
    df = pd.concat([df, multiple], axis=1)
    df.rename(columns = {'DSL': 'dsl', 'Fiber optic': 'fiber_optic'}, inplace = True)
    # Add new categorcial variable internet_service
    df['internet_service'] = df.internet_service_type != 'None'
    result = df['internet_service'].astype(int)
    df['internet_service'] = result
    df.drop(columns = ['internet_service_type'], inplace = True)
    # Change total_charges to float from object
    df['total_charges'] = pd.to_numeric(df['total_charges'],errors='coerce')
    # Add feature of tenure in terms of years
    df['tenure_years'] = round(df.tenure / 12, 2)
    # Fill NaN values in total_charges with 0
    df["total_charges"].fillna(0, inplace = True) 
    #split data
    train, validate, test = train_valid_test(df)
    train, validate, test = scale(train, validate, test)
    return train, validate, test