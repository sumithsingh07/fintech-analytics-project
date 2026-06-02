import pandas as pd
import os
folder = "data/raw"
for file in os.listdir(folder):
    if file.endswith(".csv"):
        print("\n" + "="*50)
        print("FILE:", file)
        df = pd.read_csv(
            os.path.join(folder, file)
        )
        print("Shape:")
        print(df.shape)
        print("\nColumns:")
        print(df.columns.tolist())
        print("\nDtypes:")
        print(df.dtypes)
        print("\nMissing Values:")
        print(df.isnull().sum())
        print("\nDuplicate Rows:")
        print(df.duplicated().sum())
        print("\nHead:")
        print(df.head())
