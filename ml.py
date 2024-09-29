from selenium import webdriver
import chromedriver_autoinstaller
import time
import pandas as pd
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from datetime import datetime
chromedriver_autoinstaller.install()
import os
import re
def scrape_mercadolivre(link, output_csv):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Rodar em modo headless (sem interface gráfica)
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    navegador = webdriver.Chrome(options=options)  
    navegador.get(link)
    conteudo_html = navegador.page_source
    soup = BeautifulSoup(conteudo_html, "html.parser")
    soup.find_all("a", class_="ui-search-link__title-card ui-search-link")
    links = soup.find_all("a", class_="ui-search-link__title-card ui-search-link")
    lista = [link.get_text() for link in links]
    df = pd.DataFrame(lista,columns=['Titulo'])
    precos = soup.find_all("span", class_="andes-money-amount ui-search-price__part ui-search-price__part--medium andes-money-amount--cents-superscript")
    lista2 = [preco.get_text() for preco in precos]
    df2 = pd.DataFrame(lista2,columns=['Preco'])
    df_final = pd.concat([df,df2], axis=1)
    pasta = '/home/weslei/produtos'
    caminho_completo = os.path.join(pasta, output_csv)
    df_final.to_csv(caminho_completo, index=False)
    print(f'{output_csv} salvo em {pasta}')


    
    navegador.quit()

link_geladeira = 'https://lista.mercadolivre.com.br/microondas#D[A:microondas]'
link_fogao = 'https://lista.mercadolivre.com.br/fogao#D[A:fogao]'
link_lavaloucas = 'https://lista.mercadolivre.com.br/lava-lou%C3%A7as#D[A:lava%20lou%C3%A7as]'
link_microondas = 'https://lista.mercadolivre.com.br/microondas#D[A:microondas]'



scrape_mercadolivre(link_geladeira, 'geladeira.csv')
scrape_mercadolivre(link_fogao, 'fogao.csv')
scrape_mercadolivre(link_lavaloucas, 'lavaloucas.csv')
scrape_mercadolivre(link_microondas, 'microondas.csv')
