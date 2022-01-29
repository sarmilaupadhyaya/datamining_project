## this is teh analysis for student vs accomodation
## first we filter the column required for this research question and then scale it 
from data_scaling import *

SELECTED_COLUMNS = ["SURF","NBPI","NPERR","CS1","DIPL_15","EMPL"]
df = read_csv("GrandEST.csv",";", SELECTED_COLUMNS)
## filter study 
## remove less than 2 years old and create smaller agegroup
df=df[df["NBPI"]!="ZZ"]
df=df[df["NPERR"]!="Z"]
df=df[df["SURF"]!="Z"]
df = df[df["DIPL_15"] !="Z"]
print(df["EMPL"].unique())
df = df[df["EMPL"]!= "ZZ"]
df = df.dropna()

df["NBPI"]=df["NBPI"].replace("09","9").replace("08","8").replace("07","7").replace("06","6").replace("05","5").replace("04","4").replace("03","3").replace("02","2").replace("01","1")

df["NBPI"] = df["NBPI"].replace("1","1to2").replace("2","1to2").replace("3","3to5").replace("4","3to5").replace("5","3to5").replace("6","6to10").replace("7","6to10").replace("8","6to10").replace("9","6to10").replace("10","6to10").replace("11","11to15").replace("12","11to15").replace("13","11to15").replace("14","11to15").replace("15","11to15").replace("16","16to19").replace("17","16to19").replace("18","16to19").replace("19","16to19").replace("20","20tomore")


column_type = {"SURF":"ordinal","NBPI":"ordinal","NPERR":"ordinal","CS1":"nominal","DIPL_15":"ordinal","EMPL":"nominal"}


for column, typ in column_type.items():
    print(column)
    print(df[column].unique())
    if typ == "nominal":
        df = scaling_nominal(df, column)
    elif typ == "ordinal":
        df = scaling_ordinal(df, column)
print(df.columns)
df.to_csv("socio_vs_area.csv")

