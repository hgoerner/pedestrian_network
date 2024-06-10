import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

# CSV Datei einlesen
df = pd.read_csv("https://raw.githubusercontent.com/kirenz/datasets/master/whr_20.csv")

df = df.sample(n=20, random_state=12)

df_cl = df[["country_name", "logged_gdp_per_capita", "healthy_life_expectancy"]]
df_cl.isnull().sum(axis=0)
df_cl = df_cl.dropna(axis=0)
df_cl_z = df_cl.copy()

features = ["logged_gdp_per_capita","healthy_life_expectancy"]
scaler = StandardScaler()

df_cl_z[features] = scaler.fit_transform(df_cl_z[features])

from scipy.cluster import hierarchy

df_cl_z = df_cl_z.set_index('country_name')
df_cl_z.index.name = None

plt.figure(figsize=(10, 7))
plt.title("Dendrogramm")
plt.xticks(fontsize=10)
Z = hierarchy.linkage(df_cl_z, 'ward')
dn = hierarchy.dendrogram(Z, labels=df_cl_z.index, orientation='right', color_threshold=1.5)

plt.show()