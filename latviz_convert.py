import pandas as pd
from json import dump
import numpy as np

def df_to_latviz(df: pd.DataFrame, filepath=None):
    """
    Converts a dataframe of a binary context to a JSON file in the format required by LatViz.
    :param df:
        Dataframe with the attributes as columns, the attribute labels as column names, the objects as rows, and the object labels as indices.
    :param outfile:
        Name of the JSON file to create.
        If None, will output the dictionary instead.
    """
    header = {
        "ObjNames": df.index.tolist(),
        "Params": {"AttrNames": df.columns.tolist()}
    }
    def row_to_json(label, content):
        #print(content)
        true_indices = [i for i, attr in enumerate(header["Params"]["AttrNames"]) if content[attr]]
        return {"Count": len(true_indices), "Inds": true_indices}
    body = {
        "Count": len(header["ObjNames"]),
        "Data":
        [row_to_json(label, content) for label, content in df.iterrows()]
    }

    if filepath:
        with open(filepath, 'w') as f:
            dump([header, body], f)
    else:
        return [header,body]

def np_to_latviz(matrix: np.ndarray, attribute_labels=None, object_labels=None, filepath=None):
    """
    Converts a numpy array of a binary context to a JSON file in the format required by LatViz.
    :param matrix:
        Numpy 2D array with the attributes as columns (first dimension) and the objects as rows (second dimension).
    :param attribute_labels:
        List of strings to use as attribute lables, in the order of columns in matrix. If None, letters will be used instead.
    :param object_labels:
        List of strings to use as object lables, in the order of rows in matrix. If None, numbers will be used instead, starting from1.
    :param outfile:
        Name of the JSON file to create.
        If None, will output the dictionary instead.
    """
    if not attribute_labels:
        def to_str(i):
            txt = "abcdefghijklmnopqrstuvwxyz"[i%26]
            if i > 26:
                return to_str(i//26) + txt
            return txt
        attribute_labels = [to_str(i) for i in range(matrix.shape[0])]
    if not object_labels:
        object_labels = [i for i in range(matrix.shape[1])]
    header = {
        "ObjNames": object_labels,
        "Params": {"AttrNames": attribute_labels}
    }
    def row_to_json(row):
        true_indices = [i for i, attr in enumerate(row) if attr]
        return {"Count": len(true_indices), "Inds": true_indices}
    body = {
        "Count": len(header["ObjNames"]),
        "Data":
        [row_to_json(row) for row in matrix]
    }

    if filepath:
        with open(filepath, 'w') as f:
            dump([header, body], f)
    else:
        return [header,body]

df_to_latviz(pd.read_csv("student_vs_accomodation.csv"), "student_vs_accomodation.json")
