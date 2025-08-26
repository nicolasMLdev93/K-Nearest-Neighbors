from model import model
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random

df = pd.read_csv('../data/clean_dataset.csv') 

def evaluate_neighbors(model,df):
    # Tomo la columna de 1 en adelante que solo va a ser la de los pixeles
    X = df.iloc[:,1:]
    # Transformo la fila a un arreglo
    X_eval = np.array([np.fromstring(pixel, dtype=int, sep=' ') for pixel in X['pixels']])
    # índice aleatorio
    index = random.randint(0, 200)
    face = X_eval[index]
    # Convierto al arreglo en 1 fila y n columnas (tantas como pixeles tenga)
    face_2d = face.reshape(1, -1)
    # Predicciones y probabilidades
    clase_predicha = model.predict(face_2d)
    probabilidades = model.predict_proba(face_2d)
    # Convierto el arreglo en una matriz de 48 x 48
    imagen_2d = face.reshape(48, 48)
    # Mostrar imagen
    plt.imshow(imagen_2d, cmap='gray')
    plt.axis('off')
    plt.title(f"Predicción: {clase_predicha[0]}")
    plt.show()
    return clase_predicha,probabilidades
result = evaluate_neighbors(model,df)
clase,prob = result

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

eval_clase(clase)


def show_prob(prob):
    for i in range(len(prob)):
        print(f"Probabilidad rostro ENOJADO es: {prob[i][0].round(2) * 100} %, "
            f"ASCO es: {prob[i][1].round(2)* 100} %, "
            f"MIEDO es: {prob[i][2].round(2)* 100} %, "
            f"FELIZ es: {prob[i][3].round(2)* 100} %, "
            f"TRISTE es: {prob[i][4].round(2)* 100} %, "
            f"SORPRENDIDO es: {prob[i][5].round(2)* 100} %\n")
show_prob(prob)

