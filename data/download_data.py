import gdown

url = "https://drive.google.com/uc?id=1MMuWGYqiQ4Kya_qA7aNWslGbToOsIb8C"
output = "clean_dataset.csv"

gdown.download(url, output, quiet=False)
