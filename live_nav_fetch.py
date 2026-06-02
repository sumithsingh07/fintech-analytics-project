'''import requests
import pandas as pd

url = "https://api.mfapi.in/mf/125497"

response = requests.get(url)

print("Status Code:", response.status_code)

data = response.json()

df = pd.DataFrame(data["data"])

print(df.head())

df.to_csv(
    "data/raw/hdfc_top100_live_nav.csv",
    index=False
)

print("File saved successfully")'''
import requests
import pandas as pd

schemes = {
    "HDFC_Top100":125497,
    "SBI_Bluechip":119551,
    "ICICI_Bluechip":120503,
    "Nippon_LargeCap":118632,
    "Axis_Bluechip":119092,
    "Kotak_Bluechip":120841
}

for name, code in schemes.items():

    url = f"https://api.mfapi.in/mf/{code}"

    response = requests.get(url)

    if response.status_code == 200:

        data = response.json()

        df = pd.DataFrame(data["data"])

        filename = f"data/raw/{name}.csv"

        df.to_csv(filename, index=False)

        print(f"Saved {name}")

    else:
        print(f"Failed {name}")
