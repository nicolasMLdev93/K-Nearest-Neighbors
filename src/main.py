import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from classes.knn_class import K_nearest_n
import pandas as pd
import numpy as np
from tests.random_img import face_2d,imagen_2d
import matplotlib.pyplot as plt

df = pd.read_csv('../data/clean_dataset.csv')  

def get_features(df):
    # Emoción => variable dependiente
    Y_train = df.iloc[:,0]
    # Variables independientes (píxeles)
    X = df.iloc[:,1:]
    X_train = np.array([np.fromstring(pixel, dtype=int, sep=' ') for pixel in X['pixels'] ]) / 255.0
    return X_train,Y_train

X_train,Y_train = get_features(df)

# Instanciamos el modelo
knn_instance = K_nearest_n()

# Entrenamos el modelo
knn_instance.train_model(X_train,Y_train)

# Predecimos las clases y porcentaje de probabilidades de c/u de ellas
clase_predicha = knn_instance.predict_face(face_2d)
probabilidades = knn_instance.predict_prob(face_2d)

# Imágen generada a partir del x_test
plt.imshow(imagen_2d, cmap='gray')
plt.axis('off')
plt.title(f"Predicción: {clase_predicha[0]}")
plt.show()

def eval_clase(clase_id):
    if clase_id == 0:
        print("Enojado 😡")
    elif clase_id == 1:
        print("Asco 🤢")
    elif clase_id == 2:
        print("Miedo 😱")
    elif clase_id == 3:
        print("Feliz 😃")
    elif clase_id == 4:
        print("Triste 😢")
    elif clase_id == 5:
        print("Sorprendido 😲")
    elif clase_id == 6:
        print("Neutral 😐")
    else:
        print("Desconocida ❓")

eval_clase(clase_predicha)

def show_prob(prob):
    for i in range(len(prob)):
        print(f"Probabilidad rostro ENOJADO es: {prob[i][0].round(2) * 100} %, "
            f"ASCO es: {prob[i][1].round(2)* 100} %, "
            f"MIEDO es: {prob[i][2].round(2)* 100} %, "
            f"FELIZ es: {prob[i][3].round(2)* 100} %, "
            f"TRISTE es: {prob[i][4].round(2)* 100} %, "
            f"SORPRENDIDO es: {prob[i][5].round(2)* 100} %\n")
show_prob(probabilidades)





    