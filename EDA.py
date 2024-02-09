import numpy as np
import pandas as pd

pd.set_option("display.precision", 2)

# Primer vistazo de los datos:
df = pd.read_csv("input/telecom_churn.csv")
df.head()
df.shape
df.columns
df.info()
df["Churn"] = df["Churn"].astype("int64")
df.describe()
df.describe(include=["object", "bool"])
df["Churn"].value_counts()
df["Churn"].value_counts(normalize=True)

# Ordenación de los datos:
df.sort_values(by="Total day charge", ascending=False).head()
df.sort_values(by=["Churn", "Total day charge"], ascending=[True, False]).head()

# Indexing y obtención de datos:
df["Churn"].mean()
# df[P(df['Churn'])] # Para booleans, donde P es una condición a cumplir
df[df["Churn"] == 1].mean()
df[df["Churn"] == 1]["Total day minutes"].mean()
df[(df["Churn"] == 0) & (df["International plan"] == "No")]["Total intl minutes"].max()
df.loc[0:5, ["State","Area code"]]
df.loc[0:5, "State":"Area code"]
df.iloc[0:5, 0:3]
df[-1:]

# Aplicar funciones a cada celda por columnas:
df.apply(np.max)
df.max()
df[df["State"].apply(lambda state: state[0] == "W")].head()
d = {"No": False, "Yes": True}
df["International plan"] = df["International plan"].map(d) # Se usa como diccionario
df["International plan"] = df["International plan"].map({"No": False, "Yes": True})
df = df.replace({"Voice mail plan": d})
df["Voice mail plan"] = df["Voice mail plan"].replace({"No": False, "Yes": True})
df.head()

# Agrupamiento:
columns_to_show = ["Total day minutes", "Total eve minutes", "Total night minutes"]
A = df.groupby(["Churn"])[columns_to_show].describe(percentiles=[])
B = df.groupby(["Churn"])[columns_to_show].agg([np.mean, np.std, np.min, np.max])

# Resumen de tablas:
pd.crosstab(df["Churn"], df["International plan"])
pd.crosstab(df["Churn"], df["Voice mail plan"], normalize=True)
df.pivot_table(
    ["Total day calls", "Total eve calls", "Total night calls"],
    ["Area code"],
    aggfunc="mean",
)

# DataFrame Transformations:
total_calls = (
    df["Total day calls"]
    + df["Total eve calls"]
    + df["Total night calls"]
    + df["Total intl calls"]
)
df.insert(loc=len(df.columns), column="Total calls", value=total_calls)
# loc parameter is the number of columns after which to insert the Series object
# we set it to len(df.columns) to paste it at the very end of the dataframe
df.head()



import pandas as pd
data = pd.read_csv('input/adult.data.csv')
data.head()
data.info()

data['sex'].unique()


df = data
# Contar el número de hombres y mujeres
gender_counts = df['sex'].value_counts()

# Mostrar los resultados
print("Número de hombres y mujeres:")
print(gender_counts)

avg_age = df['age'].mean()
























