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

def missing_values_table(df):
    """Returns a dataframe of number of missing entries per column in df"""
    miss_val = df.isnull().sum()
    miss_val_percent = (df.isnull().sum() * 100) / len(df)
    miss_val_table = pd.concat([miss_val, miss_val_percent], axis=1)
    miss_val_table = miss_val_table.rename(columns={0:'Missing Values', 1: '% of Missing Values'})
    
    # sort by mssing values
    miss_val_table = miss_val_table[miss_val_table.iloc[:,1] != 0].sort_values('% of Total Values', ascending=False).round(1)
     # print some summary information
    print(f'The dataframe has {str(df.shape[1])} columns.\nThere are {str(miss_val_table.shape[0])} columns with missing values')
    return miss_val_table

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