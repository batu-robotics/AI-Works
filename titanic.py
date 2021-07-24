# Pleiades Technologies
# First AI Software 

#%% importing the libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.preprocessing import LabelEncoder

#%% Data importing
def data_in(filename):
    df=pd.read_csv(filename)
    return df

#%% Inspecting data and remove unnecessary features
def construct(dataframe):
    columns=[0,1,2,4,5,6,7,9,11]
    data=dataframe.iloc[:,columns]
    return data

#%% Converting categorical values by means of label encoding
def le(dataframe):
    le=LabelEncoder()
    dataframe.iloc[:,3]=le.fit_transform(dataframe.iloc[:,3])

    # Adjusting the categorical data with NaN values 
    cat=dataframe.iloc[:,-1]
    le_cat=[]
    for i in range(len(cat)):
        if cat[i]=='S':
            le_cat.append(0)
        elif cat[i]=='C':
            le_cat.append(1)
        elif cat[i]=='Q':
            le_cat.append(2)
        else:
            le_cat.append('nan')
        
    dataframe.iloc[:,-1]=le_cat
        
    return dataframe

#%% Handling NaN values
def handle(dataframe):
    data1=dataframe.iloc[:,1]
    
    survived=[i for i in range(len(data1)) if data1[i]==1]
    dead=[j for j in range(len(data1)) if data1[j]==0]
    
    surv_data=dataframe.iloc[survived,:]
    dead_data=dataframe.iloc[dead,:]
    
    plt.figure('Data Pre-Analysis')
    sns.distplot(surv_data.iloc[:,2])
    sns.distplot(dead_data.iloc[:,2])
    plt.legend(('Survived','Dead'))
    plt.grid(True)
    
    x1=surv_data.describe()
    x2=dead_data.describe()
    
    
    return surv_data,dead_data,x1,x2

#%% Inspecting the data as statistically
def inspect(dataframe):
    pass

#%% Seperating the data as train-test
def seperate(dataframe):
    pass

#%% Final filtered dataframe construction
def data_filter(dataframe):
    pass

#%% Constructing ML model for a single analysis and CV
def ml(xtrain,xtest,ytrain,ytest):
    pass

#%% Main Program

if __name__=='__main__':
    data=data_in('train.csv')
    data2=data_in('test.csv')
    new_data=construct(data)
    label=le(new_data)
    
    k,o,x1,x2=handle(label)
 


