import os
import sys
from collections import defaultdict

import pandas as pd
import typing as t


SELECTED_COLUMNS = {"SURF":"","NBPI":"", "NPERR":"", "CS1":"", "DIPL_15":"", "EMPL":""\
        ,"ETUD":"", "TYPL":"", "INAI":"", "ILETUD":"", "AGER20":"", "ANEMR":"", "DEPT":""\
        , "TACT":"", "UR":"", "SEXE":"", "SFM":"", "TRANS":""}


ordinal = ['AGER20', 'ANEMR', 'DIPL_15', 'NBPI', 'NPERR', 'SFM', 'SURF' ]
nominal = ['CS1', 'DEPT', 'EMPL', 'ETUD', 'ILETUD', 'INAI', 'SEXE', 'TACT', 'TRANS', 'TYPL', 'UR']


def scaling_nominal(df: pd.DataFrame, column: str):
    # get all the unique values for the column
    uniques = df[column].unique()

    # copy the dataframe without the column we are replacing
    df_scaled = df[[c for c in df.columns if c!= column]].copy()

    for unique in uniques:
        df_scaled[f"{column}={unique}"] = df[column] == unique

    return df_scaled

def scaling_ordinal(df: pd.DataFrame, column: str, order_list: t.List=None):
    # get all the unique values for the column
    uniques = df[column].unique()

    # copy the dataframe without the column we are replacing
    df_scaled = df[[c for c in df.columns if c!= column]].copy()

    for unique in uniques:
        if order_list:
            df_scaled[f"{column}<={unique}"] = df[column].apply(order_list.index) <= order_list.index(unique)
        else:
            df_scaled[f"{column}<={unique}"] = df[column] <= unique

    return df_scaled

def scaling_interordinal(df: pd.DataFrame, column: str, order_list=None):
    # get all the unique values for the column
    uniques = df[column].unique()

    # copy the dataframe without the column we are replacing
    df_scaled = df[[c for c in df.columns if c!= column]].copy()

    for unique in uniques:
        if order_list:
            df_scaled[f"{column}<={unique}"] = df[column].apply(order_list.index) <= order_list.index(unique)
            df_scaled[f"{column}>={unique}"] = df[column].apply(order_list.index) >= order_list.index(unique)
        else:
            df_scaled[f"{column}<={unique}"] = df[column] <= unique
            df_scaled[f"{column}>={unique}"] = df[column] >= unique

    return df_scaled
    

def read_csv(csvpath, sep=",", columns=None):
    """
    function that reads and filters df according to column

    Params:
    csvpath (str): path to the csv file
    sep (str): separator while reading csv. Default is comma(,)
    columns (list of strings): list of columns names to be sent back

    """

    df = pd.read_csv(csvpath, sep=sep, dtype="str")
    if columns:
        return df[columns]
    else:
        return df
