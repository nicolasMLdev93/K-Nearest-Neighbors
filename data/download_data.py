import gdown

# URL de Google Drive
url = "https://drive.google.com/uc?id=1HN7BxcbCoMmzakjQwR2lK7619fD7Q_F6"
output = "fer2013.csv"  

# Descargar el archivo
gdown.download(url, output, quiet=False)
