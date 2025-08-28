from sklearn.neighbors import KNeighborsClassifier

class K_nearest_n:
    def __init__(self):
        self.model = KNeighborsClassifier(n_neighbors=100)
    def train_model(self,x_train,y_train):
        # Entrenamos el modelo de Vecinos más Cercanos
        self.model.fit(x_train,y_train)
    def predict_face(self,x_test):
        # Predicción de rostro
        return self.model.predict(x_test)
    def predict_prob(self,x_test):
        # Predicción de probabilidad de c/u de las clases
        return self.model.predict_proba(x_test)
