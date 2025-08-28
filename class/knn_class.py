from sklearn.neighbors import KNeighborsClassifier

class K_nearest_n:
    def __init__(self):
        self.model = KNeighborsClassifier(n_neighbors=5)
    