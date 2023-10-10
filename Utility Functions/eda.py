"""
This python file contains some utility functions to help with the process of data cleaning and exploration
of datasets - the first step in any machine learning pipeline.
Also includes useful plots with matplotlib and seaborn.
"""
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import seaborn as sns
import random
import os
import torch
from pandas.api.types import is_datetime64_ns_dtype

def missing_values_table(df):
    """Returns a dataframe of number of missing entries per column in df"""
    miss_val = df.isnull().sum()
    miss_val_percent = (df.isnull().sum() * 100) / len(df)
    miss_val_table = pd.concat([miss_val, miss_val_percent], axis=1)
    miss_val_table = miss_val_table.rename(columns={0:'Missing Values', 1: '% of Missing Values'})
    
    # sort by mssing values
    miss_val_table = miss_val_table[miss_val_table.iloc[:,1] != 0].sort_values('% of Missing Values', ascending=False).round(1)
     # print some summary information
    print(f'The dataframe has {str(df.shape[1])} columns.\nThere are {str(miss_val_table.shape[0])} columns with missing values')
    return miss_val_table


def reduce_mem_usage(df):
    """iterate through all the numeric columns of a dataframe and modify
    the data usage to reduce memory usage
    """
    for col in df.columns:
        col_type = df[col].dtype
        
        if col_type != object and not is_datetime64_ns_dtype(df[col]) and not 'category':
            c_min = df[col].min()
            c_max = df[col].max()
            
            if str(col_type)[:3] == 'int':
                if c_min > np.iinfo(np.int8).min and c_max < np.iinfo(np.int8).max:
                    df[col] = df[col].astype(np.int8)
                elif c_min > np.iinfo(np.int16) and c_max < np.iinfo(np.int16).max:
                    df[col] = df[col].astype(np.int16)
                elif c_min > np.iinfo(np.int32) and c_max < np.iinfo(np.int32).max:
                    df[col] = df[col].astype(np.int32)
            else:
                df[col] = df[col].astype(np.float16)
    return df




# this function does the same as above but also includes datatypes
def quality_report(df):
    """Performs a quaity report of df based on unique values, missing values, missing values % and datatype"""
    
    dtypes = df.dtypes
    nuniq = df.T.apply(lambda x: x.nunique(), axis=1)
    total_null = df.isnull().sum()
    percent_null = (100* df.isnull().sum())/len(df)
    
    quality_df = pd.concat([total_null, percent_null, nuniq,dtypes],axis=1, keys=['Total Null', 'Percent Null', 'No. of Unique'
                                                                                , 'datatypes'])
    # sort by % of missing values
    quality_df = quality_df.sort_values(by='Percent Null', ascending=False).round(1)
    return quality_df

# check if test is a subset of train
def check_subset(train, test, cols):
    """Checks if train is a subset of the test dataframe
    Returns a list of columns which are subsets"""
    subset = []

    for col in cols:
        bool = set(test[col].unique()).issubset(set(train[col].unique()))
        if bool: # if column is a subset
            subset.append(col)
    return subset

def numeric_distribution_plot(df):
    """Plots a seaborn displot for all numeric features in the dataset"""
    num_features = df.select_dtypes(exclude='object').columns # only include numeric features
    print(f"There are {len(num_features)} numeric features in the dataset")
    for feature in num_features:
        plt.figure(figsize=(12, 5))
        sns.displot(data=df, x=feature)
        plt.show()

def categorical_feature_plot(df):
    """Plots a countplot for all categorical features present in the dataframe"""
    cat_features = df.select_dtypes(include='object').columns
    for feature in cat_features:
        plt.figure(figsize=(12,5))
        sns.countplot(x = feature, data=df)
        plt.tight_layout()
        plt.show()

def kde_plot(df, col):
    """
    Needs to be heavily modified to work with the new task
    """
    # print mean information of col by target
    away_mean = df.loc[df['target'] == 0, col].mean()
    draws_mean = df.loc[df['target'] == 1, col].mean()
    home_mean = df.loc[df['target'] == 2, col].mean()
    
    print(f"The average {col} for the home wins: {round(home_mean, 2)}")
    print(f"The average {col} for the away wins: {round(away_mean, 2)}")
    print(f"The average {col} for the draws: {round(draws_mean, 2)}")
    
    # kde distribution for each of the target classes
    sns.kdeplot(df.loc[df['target'] == 0, col], label = 'target == away')
    sns.kdeplot(df.loc[df['target'] == 1, col], label = 'target == draws')
    sns.kdeplot(df.loc[df['target'] == 2, col], label = 'target == home')
    
    plt.title(f"Distribution of {col} by target")
    plt.xlabel(f"{col}")
    plt.ylabel('Density')
    plt.legend()
    plt.tight_layout(h_pad = 2.5)


def seed_everything(seed):
    """Utility to set the random seed to a certain value"""
    random.seed(seed)
    np.random.seed(seed)
    os.environ['PYTHONHASHSEED'] = str(seed)
    torch.manual_seed(seed)
    if CFG.USE_GPU:
        torch.cuda.manual_seed(seed)
        torch.backends.cudnn.deterministic = True
        torch.backends.cudnn.benchmark = False

"""
def Handling_Rare_Values(df,column,threshold): 
     df[column] = df[column].fillna("NONE")
     condition_index = df[column].value_counts()[df[column]].values < threshold
     df.loc[condition_index, column] = "RARE"
     print(df[column].value_counts())
     return df

"""


"""
beta mode
def numeric_plot(df):
    Plots a seaborn displot for all numeric features in the dataset
    from math import ceil
    num_features = df.select_dtypes(exclude='object').columns # only include numeric features
    print(f"There are {len(num_features)} numeric features in the dataset")
    
    x = len(num_features)
    rows = ceil(x/5) 
    plt.figure(figsize=(12, 5))
    for i in range(1, len(num_features) + 1):
        plt.subplot(rows, 5, i)
        sns.displot(data=df, x=num_features[i])
        plt.show()
"""