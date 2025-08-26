from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np

df = pd.read_csv('../data/clean_dataset.csv')  

def train_KNeighborsClassifier(df):
    # Emoción => variable dependiente
    Y_train = df.iloc[:,0]
    # Variables independientes (píxeles)
    X = df.iloc[:,1:]
    X_train = np.array([np.fromstring(pixel, dtype=int, sep=' ') for pixel in X['pixels'] ])
    neigh = KNeighborsClassifier(n_neighbors=5)
    neigh.fit(X_train, Y_train)
    return X_train,Y_train

model = train_KNeighborsClassifier(df)

    