## this is teh analysis for student vs accomodation
## first we filter the column required for this research question and then scale it 
from data_scaling import *

SELECTED_COLUMNS = ["ETUD","DIPL_15","TYPL","INAI","ILETUD"]
df = read_csv("GrandEST.csv",";", SELECTED_COLUMNS)

## filter study 
df = df[df["ETUD"]=="1"]
df = df[df["DIPL_15"] !="Z"]
df = df[df["TYPL"] != "Z"]

SELECTED_COLUMNS.remove("ETUD")
df = df[SELECTED_COLUMNS]

for column in df.columns:
    if column == "INAI":
        df[column] = df[column].replace("5","4")
    if column == "ILETUD":
        df[column] = df[column].replace("5","6")

column_type = {"DIPL_15":"ordinal","TYPL":"nominal", "INAI":"nominal", "ILETUD":"nominal"}


for column, typ in column_type.items():

    if typ == "nominal":
        
        df = scaling_nominal(df, column)
    elif typ == "ordinal":
        df = scaling_ordinal(df, column)

print(df.columns)
df.to_csv("student_vs_accomodation.csv")







