🤬 Proyecto de Clasificación de Emociones:

Este proyecto implementa un modelo de clasificación de imágenes que predice la categoría de una imagen dada.

😀 → Felicidad

😢 → Tristeza

😡 → Enojo

😱 → Sorpresa / Miedo

🤢 → Disgusto / Asco

😐 → Neutral

Se utiliza un dataset de imágenes en formato plano (1D) que luego se transforma a 2D para su visualización.
El modelo utilizado es K-Nearest Neighbors (KNN) de scikit-learn.

⚡ Instalación y uso:

1-Descarga el repo:

https://github.com/nicolasMLdev93/K-Nearest-Neighbors.git

2- Crear y activar entorno virtual:

python -m venv venv

venv\Scripts\activate

3- Instalar dependencias:

pip install -r requirements.txt

4- Ve a el directorio data/ y una vez allí corre el script de download_data.py, el cual descargará automáticamente 
el dataset de google drive (puede tardar unos segundos debido a que el dataframe es muy pesado y cuenta con mas de 36000 rostros)

5- Entrenar el modelo y detectar rostro:

⏱️ Puede que el modelo demore unos segundos en predecir el rostro ya que obtiene forma aleatoria una fila del dataframe original !

python src/main.py


🧑 Mi perfil:

https://www.linkedin.com/in/nicol%C3%A1s-bauz%C3%A1-48a8a0244/ 👈 – Sígueme para ver mis proyectos de desarrollo y ML. 🚀

