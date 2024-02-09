"""
Estos son solo ejemplos básicos para ilustrar transformaciones (map, filter) y acciones (collect, count, reduce).
En un entorno de Spark real, trabajarías con conjuntos de datos más grandes y complejos.
Además, ten en cuenta que Spark utiliza una evaluación perezosa (lazy evaluation),
lo que significa que las transformaciones no se ejecutan hasta que se llama a una acción.
"""
from pyspark import SparkContext

sc = SparkContext("local", "RDD Transformations and Actions Example")

data = [1, 2, 3, 4, 5]
rdd = sc.parallelize(data)

# Transformación map: duplica cada elemento del RDD
transformed_rdd = rdd.map(lambda x: x * 2)

print("Original RDD: ", rdd.collect())
print("Transformed RDD (map): ", transformed_rdd.collect())

# Transformación filter: filtra los elementos mayores que 2
filtered_rdd = rdd.filter(lambda x: x > 2)

print("Original RDD: ", rdd.collect())
print("Transformed RDD (filter): ", filtered_rdd.collect())

# Acción collect: recopila todos los elementos del RDD en una lista
collected_data = transformed_rdd.collect()

print("Collected Data: ", collected_data)

# Acción count: devuelve el número de elementos en el RDD
count = rdd.count()

print("Number of Elements: ", count)

# Acción reduce: suma todos los elementos del RDD
total_sum = rdd.reduce(lambda x, y: x + y)

print("Total Sum: ", total_sum)
