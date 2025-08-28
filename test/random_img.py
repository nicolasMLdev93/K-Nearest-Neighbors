import random
import pandas as pd
import numpy as np

# Del dataframe se obtiene una fila la cual será la imagen que usaremos como evaluación del modelo
# El índice se obtiene de forma aleatoria a modo de cambiar la imagen constantemente

# Obtengo los pixeles de la imagen 
df = pd.read_csv('../data/clean_dataset.csv')
X = df.iloc[:,1:]

# Transformo la fila a un arreglo
X_eval = np.array([np.fromstring(pixel, dtype=int, sep=' ') for pixel in X['pixels']])
# índice aleatorio
index:int = random.randint(0, 200)
face = X_eval[index]
# Convierto al arreglo en 1 fila y n columnas (tantas como pixeles tenga)
face_2d = face.reshape(1, -1)


