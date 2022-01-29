## this is teh analysis for student vs accomodation
## first we filter the column required for this research question and then scale it 
from data_scaling import *

SELECTED_COLUMNS = ["AGER20","ANEMR","DEPT","NBPI","NPERR","SURF","TACT","TYPL","UR"]
df = read_csv("GrandEST.csv",";", SELECTED_COLUMNS)

## filter study 
## remove less than 2 years old and create smaller agegroup
#df = df[df["AGER20"]!="2"]
#df = df[df["ANEMR"]!=99]
df=df[df["ANEMR"]!="ZZ"]
df=df[df["NBPI"]!="ZZ"]
df=df[df["NPERR"]!="Z"]
df=df[df["SURF"]!="Z"]
df=df[df["TYPL"]!="Z"]
df["ANEMR"]=df["ANEMR"].replace("00","0").replace("09","9").replace("08","8").replace("07","7").replace("06","6").replace("05","5").replace("04","4").replace("03","3").replace("02","2").replace("01","1")

df["NBPI"]=df["NBPI"].replace("09","9").replace("08","8").replace("07","7").replace("06","6").replace("05","5").replace("04","4").replace("03","3").replace("02","2").replace("01","1")


df["AGER20"] = df["AGER20"].replace("2","0to14").replace("10","0to14").replace("14","0to14").replace("17","15to19").replace("5","0to14").replace("19","15to19").replace("24","20to24").replace("29","25to29").replace("39","30to39").replace("54","40to54").replace("64","55to79").replace("79","55to79").replace("80","80toold")


df["ANEMR"] = df["ANEMR"].replace("0","lessthan2").replace("1","2to4").replace("2","5to9").replace("3","10to19").replace("4","20to29").replace("5","30tomore").replace("6","30tomore").replace("7","30tomore").replace("8","30tomore").replace("9","30tomore")

df["NBPI"] = df["NBPI"].replace("1","1to2").replace("2","1to2").replace("3","3to5").replace("4","3to5").replace("5","3to5").replace("6","6to10").replace("7","6to10").replace("8","6to10").replace("9","6to10").replace("10","6to10").replace("11","11to15").replace("12","11to15").replace("13","11to15").replace("14","11to15").replace("15","11to15").replace("16","16to19").replace("17","16to19").replace("18","16to19").replace("19","16to19").replace("20","20tomore")


column_type = {"AGER20":"ordinal","ANEMR":"ordinal","DEPT":"nominal","NBPI":"ordinal","NPERR":"ordinal","SURF":"ordinal","TACT":"nominal","TYPL":"nominal","UR":"nominal"}

df_em = pd.DataFrame([])

for column, typ in column_type.items():
    print(column)
    print(df[column].unique())
    if typ == "nominal":
        df = scaling_nominal(df,column)
        #df_em = pd.concat([df_em, scaling_nominal(df, column)], axis=1)

    elif typ == "ordinal":
        df = scaling_ordinal(df,column)
        #df_em = pd.concat([scaling_ordinal(df, column)],axis=1)

print(df.columns)
df.to_csv("agegroup_vs_housing.csv")


