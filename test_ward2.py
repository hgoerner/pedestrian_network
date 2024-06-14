import pandas as pd
from sklearn.preprocessing import StandardScaler
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.cluster import hierarchy
from sklearn.cluster import AgglomerativeClustering

# CSV Datei einlesen
df = pd.read_csv("https://raw.githubusercontent.com/kirenz/datasets/master/whr_20.csv")



plt.figure(figsize=(8,8))

sns.scatterplot(
    data=df, 
    x="logged_gdp_per_capita", y="healthy_life_expectancy",
)

df = df.sample(n=20, random_state=12)

plt.figure(figsize=(6,6))

sns.set_theme(style="ticks", font_scale=1.00)

g = sns.scatterplot(
    data=df, 
    x="logged_gdp_per_capita", y="healthy_life_expectancy", hue="country_name",
    palette="crest", s=100
)

plt.title("Lebenszufriedenheit (2020)")
plt.xlabel("Bruttoinlandsprodukt pro Einwohner (logarithmiert)")
plt.ylabel("Lebenserwartung in Jahren")

plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.show()
df_cl = df[["country_name", "logged_gdp_per_capita", "healthy_life_expectancy"]]

df_cl.isnull().sum(axis=0)
df_cl.isnull().sum(axis=1)
df_cl = df_cl.dropna(axis=0)
df_cl_z = df_cl.copy()

features = ["logged_gdp_per_capita","healthy_life_expectancy"]
scaler = StandardScaler()
df_cl_z[features] = scaler.fit_transform(df_cl_z[features])
df_cl_z.head()

plt.figure(figsize=(6,6))

sns.set_theme(style="ticks", font_scale=1.00)

g = sns.scatterplot(
    data=df_cl_z, 
    x="logged_gdp_per_capita", y="healthy_life_expectancy", hue="country_name",
    palette="crest", s=100
)

plt.title("Lebenszufriedenheit (2020)")
plt.xlabel("Bruttoinlandsprodukt pro Einwohner (logarithmiert)")
plt.ylabel("Lebenserwartung in Jahren")
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.show()
df_cl_z = df_cl_z.set_index('country_name')
df_cl_z.index.name = None

print(df_cl_z.head())
print(df_cl_z.shape)


plt.figure(figsize=(10, 7))
plt.title("Dendrogramm")

Z = hierarchy.linkage(df_cl_z, 'ward')
dn = hierarchy.dendrogram(Z, labels=df_cl_z.index, orientation='right')

plt.show()



clustering = AgglomerativeClustering(n_clusters=4, linkage='ward')
clustering.fit_predict(df_cl_z)

print(clustering.labels_)

df_cl["cluster"] = clustering.labels_
print(df_cl.head())

plt.figure(figsize=(6,6))

sns.set_theme(style="ticks", font_scale=1.00)

g = sns.scatterplot(
    data=df_cl, 
    x="logged_gdp_per_capita", y="healthy_life_expectancy", hue="cluster", 
    palette="crest", s=100
)

plt.title("Lebenszufriedenheit (2020)")
plt.xlabel("Bruttoinlandsprodukt pro Einwohner (logarithmiert)")
plt.ylabel("Lebenserwartung in Jahren")

plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

plt.show()

plt.figure(figsize=(8,8))

sns.set_theme(style="ticks", font_scale=1.00)

g = sns.scatterplot(
    data=df_cl, 
    x="logged_gdp_per_capita", y="healthy_life_expectancy", hue="country_name", style="cluster",
    palette="crest", s=100
)

plt.title("Lebenszufriedenheit (2020)")
plt.xlabel("Bruttoinlandsprodukt pro Einwohner (logarithmiert)")
plt.ylabel("Lebenserwartung in Jahren")

plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

plt.show()

