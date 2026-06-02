<<<<<<< HEAD
=======
'''import pandas as pd
import os
folder = "data/raw"
for file in os.listdir(folder):
    if file.endswith(".csv"):
        df = pd.read_csv(
            os.path.join(folder,file)
        )
        print("\n"+"="*50)
        print("FILE:",file)
        print("Shape:")
        print(df.shape)
        print("\nDtypes:")
        print(df.dtypes)
        print("\nHead:")
        print(df.head())'''
>>>>>>> 0bc37ddbf6b6c878d2757f52d3430d65ef93a4b7
import pandas as pd
import os
folder = "data/raw"
for file in os.listdir(folder):
    if file.endswith(".csv"):
<<<<<<< HEAD
        print("\n" + "="*50)
        print("FILE:", file)
        df = pd.read_csv(
            os.path.join(folder, file)
        )
        print("Shape:")
        print(df.shape)
        print("\nColumns:")
        print(df.columns.tolist())
=======
        path = os.path.join(folder, file)
        df = pd.read_csv(path)
        print("\n" + "="*60)
        print("FILE:", file)
        print("Shape:", df.shape)
>>>>>>> 0bc37ddbf6b6c878d2757f52d3430d65ef93a4b7
        print("\nDtypes:")
        print(df.dtypes)
        print("\nMissing Values:")
        print(df.isnull().sum())
        print("\nDuplicate Rows:")
        print(df.duplicated().sum())
        print("\nHead:")
        print(df.head())
