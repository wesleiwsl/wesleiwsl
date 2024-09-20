import pandas as pd
import glob
import requests
import os
from datetime import datetime
import time
now = datetime.now()
hoje = now.strftime('%Y-%m-%d %H:%M:%S')
print(f'Timestamp atual: {hoje}')

urls = ['https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/shpc/qus/ultimas-4-semanas-diesel-gnv.csv',
       'https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/shpc/qus/ultimas-4-semanas-gasolina-etanol.csv'
      ]

for url in urls:
    try:
        # Obtém o nome do arquivo a partir da URL
        nome_arquivo = hoje + '_' + url.split('/')[-1]
        caminho_arquivo = os.path.join('/home/weslei/wesleiwsl/preco_anp/download/', nome_arquivo)
        #caminho_arquivo = os.path.join('<coloque aqui o seu diretorio>', nome_arquivo)
        # Baixa o arquivo
        response = requests.get(url)
        response.raise_for_status()  # Verifica se ocorreu algum erro na solicitação
        
         #Salva o arquivo no caminho especificado
        with open(caminho_arquivo, 'wb') as file:
            file.write(response.content)
        
        print(f'Arquivo {nome_arquivo} salvo com sucesso.')
    
    except Exception as e:
        print(f'Erro ao baixar o arquivo {url}: {e}')

#buscar todos arquivos da pasta

time.sleep(5)

caminho = '/home/weslei/wesleiwsl/preco_anp/download/*.csv'
#caminho = '<coloque aqui o seu diretorio>/*.csv'


arquivos_csv = glob.glob(caminho)
dfs = [pd.read_csv(arquivo, sep=';') for arquivo in arquivos_csv]
df= pd.concat(dfs, ignore_index=True)
#filtrando csv
colunas = ['Estado - Sigla','Municipio','Revenda','CNPJ da Revenda','Produto','Valor de Venda','Unidade de Medida','Bandeira','Data da Coleta']
df2= df[colunas]
df3 = df2.sort_values(by='Data da Coleta')
#criar coluna para evitar dados duplicados no csv final
df3['Id'] = df3['CNPJ da Revenda'] + ' - ' + df3['Produto'] + ' - ' + df3['Data da Coleta'].astype(str)
df4 = df3.drop_duplicates(subset='Id')
#df4.to_csv('<colque aqui o seu diretorio>/preco.csv', index = False)
df4.to_csv('/home/weslei/sambashare/preco.csv', index = False)

