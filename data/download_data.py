import gdown

# Descarga el clean_dataset.csv de google cloud ya que es muy pesado para guardar en el repositorio

url = "https://drive.google.com/uc?id=1MMuWGYqiQ4Kya_qA7aNWslGbToOsIb8C"
output = "clean_dataset.csv"

gdown.download(url, output, quiet=False)
