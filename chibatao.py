from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
from bs4 import BeautifulSoup
import pandas as pd
import re
import os
import time

# Instalar o ChromeDriver automaticamente
chromedriver_autoinstaller.install()

# Configurar o WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Rodar em modo headless (sem interface gráfica)
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

print('iniciando navegador')
# Iniciar o ChromeDriver com as opções
driver = webdriver.Chrome(options=options)

# Navegar para o site
driver.get('http://modallport.grupochibatao.com.br:2424/modallsgt/Public/SGTP002')

print('html pagina')
# Obter o código-fonte da página
html = driver.page_source

# Analisar o HTML com BeautifulSoup (não é estritamente necessário para o restante do código, mas pode ser útil)
soup = BeautifulSoup(html, 'html.parser')
time.sleep(3)
# Localizar todas as linhas <tr> na tabela
linhas = driver.find_elements(By.TAG_NAME, "tr")

# Criar uma lista para armazenar os dados
dados = []

# Iterar sobre as linhas e coletar os dados
for linha in linhas:
    colunas = linha.find_elements(By.TAG_NAME, "th") + linha.find_elements(By.TAG_NAME, "td")
    conteudo = [coluna.text for coluna in colunas]
    dados.append(conteudo)

# Fechar o WebDriver
driver.quit()
print('fechando navegador')

# Criar um DataFrame a partir da lista de dados
df = pd.DataFrame(dados)

# Exportar o DataFrame para um arquivo CSV
df.to_csv('chibatao.csv', index=False, header=False)

print("Dados exportados para chibatao.csv")
