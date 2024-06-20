import pandas as pd
from scipy import stats
import pandas as pd
import numpy as np

path_to_excel = r"Z:\_Public\Projekte\IVST\058_FoPS_Fuss\02_Bearbeitung\AP5\Matrix_Zählstellen.xlsx"
df = pd.read_excel(path_to_excel, na_values='-')
# Erstellen eines Beispieldatensatzes

df.dropna(subset=['Entfernung Bushaltestelle'], inplace=True)
print(df["Entfernung Bushaltestelle"])
df["Entfernung Bushaltestelle"]  = df["Entfernung Bushaltestelle"].astype(int)

print(df.info())
print(df["Entfernung Bushaltestelle"])
groups = df['Umfeldkategorie'].unique()

print(groups)

# ANOVA durchführen mit Scipy
f_val, p_val = stats.f_oneway(*(df[df['Umfeldkategorie'] == group]['Entfernung Bushaltestelle'] for group in groups))

print('F-Wert:', f_val)
print('P-Wert:', p_val)