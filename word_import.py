import re
import requests
import pandas as pd
from bs4 import BeautifulSoup

# Pegando o link, e permite a leitura dele
url = "https://www.dicio.com.br/palavras-dificeis-para-o-jogo-da-forca/"
page = requests.get(url)
soup = BeautifulSoup(page.text, "lxml")

# table = soup.find("table",class_: "table-normal")