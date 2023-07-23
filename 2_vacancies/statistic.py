import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

response = requests.get("https://uadata.net/work-positions/cities.json?o=Київ")
data_json = response.json()

df = pd.DataFrame(data_json["data"])
print(df.head())
print(df.shape)
print(df.columns)
print(df.dtypes)
df["at"] = pd.to_datetime(df["at"])
print(df.dtypes)
df = df.rename(columns = {"at": "Дата","val": "Вакансії"})
print(df.head())
df.set_index('Дата', inplace=True)
print(df.head())
# Create of graphs
# graph start
df["Вакансії"].plot()
plt.title("Кількість вакансій по Києву")
plt.xlabel("Дата")
plt.ylabel("Вакансії")
plt.ylim(bottom=0)
plt.show()
# graph end
df["Вакансії"] = df["Вакансії"].replace(0, np.nan)
df["Вакансії"] = df["Вакансії"].interpolate()
# graph2 start
df["Вакансії"].plot()
plt.title("Кількість вакансій по Києву")
plt.xlabel("Дата")
plt.ylabel("Вакансії")
plt.ylim(bottom=0)
plt.show()
# graph2 end
df["rolling_mean"] = df["Вакансії"].rolling(window=7).mean()
print(df)
# graph3 start
df["rolling_mean"].plot()
plt.title("Кількість вакансій по Києву")
plt.xlabel("Дата")
plt.ylabel("Вакансії")
plt.ylim(bottom=0)
plt.show()
# graph3 end
print(df.describe())