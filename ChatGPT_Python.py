import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Primer vistazo de los datos:
df = pd.read_csv("input/telecom_churn.csv")
df.head()
df.info()

# Configuración de estilo para seaborn
sns.set(style="whitegrid")

# Gráfico de barras para la distribución de Churn
plt.figure(figsize=(8, 5))
sns.countplot(x='Churn', data=df, palette='viridis')
plt.title('Distribución de Churn')
plt.xlabel('Churn')
plt.ylabel('Conteo')
plt.show()

# Gráfico de barras para la distribución de Estados
plt.figure(figsize=(14, 6))
sns.countplot(x='State', data=df, palette='viridis', order=df['State'].value_counts().index)
plt.title('Distribución de Estados')
plt.xlabel('Estado')
plt.ylabel('Conteo')
plt.xticks(rotation=90)
plt.show()

# Gráfico de correlación entre variables numéricas
plt.figure(figsize=(16, 10))
correlation_matrix = df.select_dtypes(include=[np.number]).corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Matriz de correlación')
plt.show()

# Boxplot para Total day minutes y Churn
plt.figure(figsize=(8, 5))
sns.boxplot(x='Churn', y='Total day minutes', data=df, palette='viridis')
plt.title('Boxplot de Total day minutes por Churn')
plt.xlabel('Churn')
plt.ylabel('Total day minutes')
plt.show()

# Gráfico de dispersión para Total day minutes y Total day charge
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Total day minutes', y='Total day charge', hue='Churn', data=df, palette='viridis')
plt.title('Dispersión entre Total day minutes y Total day charge')
plt.xlabel('Total day minutes')
plt.ylabel('Total day charge')
plt.show()

categorical_columns = df.select_dtypes(include=['object']).columns
for column in categorical_columns:
    print(f'\n{column}:\n{df[column].value_counts()}\n')

# Agrupa por código de área y suma los totales de llamadas
calls_by_area = df.groupby('Area code')[['Total day calls', 'Total eve calls', 'Total night calls']].mean()

# Muestra la tabla resultante
print(calls_by_area)

# Crear la nueva columna 'Total calls' que contiene la suma de las llamadas
Total_Calls = df['Total day calls'] + df['Total eve calls'] + df['Total night calls'] + df['Total intl calls']

# Obtener la posición de la columna 'Number vmail messages'
index_of_vmail_messages = df.columns.get_loc('Number vmail messages')

# Insertar la nueva columna directamente a la derecha de 'Number vmail messages'
df.insert(index_of_vmail_messages + 1, 'Total calls', Total_Calls)

# Mostrar el DataFrame resultante
print(df.head())

# Filtrar y eliminar filas con total de llamadas superior a 330
df = df.loc[df['Total calls'] <= 330]

# Mostrar el DataFrame resultante
print(df.head())

# Reemplazar "yes" por True y "no" por False en todo el DataFrame
df.replace({'yes': True, 'no': False}, inplace=True)

# Mostrar el DataFrame resultante
print(df.head())

df.info()

# Gráfico de barras para la relación entre 'Churn' y 'International plan'
plt.figure(figsize=(8, 5))
sns.countplot(x='International plan', hue='Churn', data=df)

# Agregar leyenda
plt.legend(title='Churn', labels=['No Churn', 'Churn'], loc='upper right')

plt.title('Relación entre Churn e International plan')
plt.xlabel('International plan')
plt.ylabel('Conteo')
plt.show()

contingency_table = pd.crosstab(df['International plan'], df['Churn'], margins=True, margins_name='Total')
percentage_churn = df.groupby('International plan')['Churn'].mean() * 100

print(df['Churn'].value_counts())

df['Churn'].replace({'True': True, 'False': False}, inplace=True)
df['Churn'] = df['Churn'].astype(bool)

# Gráfico de barras para la relación entre 'Churn' y 'Customer service calls'
plt.figure(figsize=(10, 6))
sns.countplot(x='Customer service calls', hue='Churn', data=df, palette='viridis')

# Agregar leyenda
plt.legend(title='Churn', labels=['No Churn', 'Churn'], loc='upper right')

plt.title('Relación entre Churn y Customer service calls')
plt.xlabel('Customer service calls')
plt.ylabel('Conteo')
plt.show()








