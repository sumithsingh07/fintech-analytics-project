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
import pandas as pd
import os
folder = "data/raw"
for file in os.listdir(folder):
    if file.endswith(".csv"):
        path = os.path.join(folder, file)
        df = pd.read_csv(path)
        print("\n" + "="*60)
        print("FILE:", file)
        print("Shape:", df.shape)
        print("\nDtypes:")
        print(df.dtypes)
        print("\nMissing Values:")
        print(df.isnull().sum())
        print("\nDuplicate Rows:")
        print(df.duplicated().sum())
        print("\nHead:")
        print(df.head())
