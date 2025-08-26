from sklearn.neighbors import KNeighborsClassifier
import pandas as pd

df = pd.read_csv('../data/fer2013.csv')

def clean_dataset(df):
    # Eliminación de datos nulos y redundantes:
    df.dropna(inplace=True)
    df.drop_duplicates(inplace=True)

    # Eliminación de columna 'Usage' => irrelevante para el entrenamiento del modelo
    df.drop('Usage', axis=1, inplace=True)
    return df

clean = clean_dataset(df)
clean.to_csv('clean_dataset.csv',index=False,encoding='utf-8-sig')