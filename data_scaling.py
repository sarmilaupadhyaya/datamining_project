import os
import sys
from collections import defaultdict

import pandas as pd



SELECTED_COLUMNS = {"SURF":"","NBPI":"", "NPERR":"", "CS1":"", "DIPL_15":"", "EMPL":""\
        ,"ETUD":"", "TYPL":"", "INAI":"", "ILETUD":"", "AGER20":"", "ANEMR":"", "DEPT":""\
        , "TACT":"", "UR":"", "SEXE":"", "SFM":"", "TRANS":""}


ordinal = ['AGER20', 'ANEMR', 'DIPL_15', 'NBPI', 'NPERR', 'SFM', 'SURF' ]
nominal = ['CS1', 'DEPT', 'EMPL', 'ETUD', 'ILETUD', 'INAI', 'SEXE', 'TACT', 'TRANS', 'TYPL', 'UR']


def nominal_operator(attribute, value):
    """
    """
    if attribute == value:
        return True
    else:
        return False
    
def ordinal_scaling(attribute_value, value):
    """
    """
    if value <= attribute_value:
        return True
    else:
        return False
    
    
def interordinal_scaling(first_att, second_att, value):
    
    if (value <= first_att) and (value >= second_att):
        return True
    else:
        return False
    
    

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

def scaling(df, ordinal,nominal):
    """

    """
    # getting unique values from each column and storing in a dictionary

    columns_attribute = defaultdict()
    for column in df:
        print(column)
        unique = df[column].unique()
        columns_attribute[column] = unique
        print("Unique value for column:", column, " are:")
        print(unique)
        print("---------------------------------------")

    rows = []
    new_df = pd.DataFrame([])

    for column, unique in columns_attribute.items():

        if column in nominal:
            for each in unique:
                key_name = column+ "_" + str(each)
                new_df[key_name] = df.apply(lambda x: nominal_operator(each, x[column]), axis=1)

    for column, unique in columns_attribute.items():
        if column in ordinal:
            for each in unique:
                key_name = column+ "_<=_" + str(each)
                new_df[key_name] = df.apply(lambda x: ordinal_scaling(each, x[column]), axis=1)



df = read_csv("GrandEST.csv", sep=";", columns = list(SELECTED_COLUMNS.keys()))
# get the unique value and do scaling accordingly

# this is test for two columns, comment these 3 lines to run on all
ordinal = ['AGER20']
nominal = ['CS1']
SELECTED_COLUMNS = ['CS1']

result = scaling(df[SELECTED_COLUMNS], ordinal, nominal)

print(result)
