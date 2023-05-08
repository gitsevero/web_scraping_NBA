import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json
from time import sleep


# 1. pegar conteúdo HTML a partir da URL
url = "https://stats.nba.com/players/traditional/?PerMode=Totals&Season=2019-20&SeasonType=Regular%20Season&sort=PLAYER_NAME&dir=-1"

driver = webdriver.Chrome()

driver.get(url)

# esperar 5 segundos para a página ser carregada completamente
sleep(5)
# localizar tabela document.querySelector('th[field="PTS"]').parentElement.parentElement.parentElement.
tabela = driver.execute_script(
    "return document.querySelector('th[field=\"PTS\"]').parentElement.parentElement.parentElement.outerHTML"
)

# parsear o conteúdo HTML - BeautifulSoup
soup = BeautifulSoup(tabela, "html.parser")
table = soup.find(name="table")

# estruturar conteúdo em um Data Frame - Pandas
df_full = pd.read_html(str(table))[0].head(10)
df = df_full[["Unnamed: 0", "Player", "Team", "PTS"]]
df.columns = ["pos", "player", "team", "total"]

print(df)
