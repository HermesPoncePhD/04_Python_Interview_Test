import numpy as np
from sklearn.linear_model import LinearRegression

# Crear el modelo de regresión lineal
model = LinearRegression()

# Entrenar el modelo con los datos
X = np.array([[1], [2], [3]])  # Datos de entrada
y = np.array([2, 4, 6])  # Datos de salida
X = X.reshape(-1, 1)  # Reshape the input data
model.fit(X, y)

# Obtener el valor de la intersección
intercept = model.intercept_
print(intercept)

