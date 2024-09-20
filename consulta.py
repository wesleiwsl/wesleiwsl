import requests

def buscar_cep():
    cep_site = 'https://brasilapi.com.br/api/cep/v2/'

    while True:  # Loop para tentar novos CEPs ou sair
        cep = input("INFORME O CEP ou 'sair' para terminar: ")

        # Verificar se o usuário quer encerrar
        if cep.lower() == 'sair':
            print("Encerrando a busca por CEP.")
            break

        # Fazer a requisição
        r_cep = requests.get(cep_site + cep)

        # Verificar se a requisição foi bem-sucedida
        if r_cep.status_code == 200:
            # Decodificar o JSON diretamente da resposta
            dados = r_cep.json()

            # Exibir os dados
            print(f"\nCEP: {dados['cep']}")
            print(f"Estado: {dados['state']}")
            print(f"Cidade: {dados['city']}")
            print(f"Bairro: {dados['neighborhood']}")
            print(f"Rua: {dados['street']}\n")
        else:
            print("Erro na requisição. Verifique o CEP e tente novamente.\n")


def buscar_cnpj():
    cnpj_site = 'https://brasilapi.com.br/api/cnpj/v1/'

    while True:  # Loop para tentar novos CNPJs ou sair
        cnpj = input("INFORME O CNPJ ou 'sair' para terminar: ")

        # Verificar se o usuário quer encerrar
        if cnpj.lower() == 'sair':
            print("Encerrando a busca por CNPJ.")
            break

        # Fazer a requisição
        r_cnpj = requests.get(cnpj_site + cnpj)

        # Verificar se a requisição foi bem-sucedida
        if r_cnpj.status_code == 200:
            # Decodificar o JSON diretamente da resposta
            dados = r_cnpj.json()

            # Exibir os dados
            print(f"\nRazão Social: {dados['razao_social']}")
            print(f"Nome Fantasia: {dados['nome_fantasia']}")
            print(f"CNPJ: {dados['cnpj']}")
            print(f"Capital Social: R${dados['capital_social']:,}")
            print(f"Endereço: {dados['logradouro']}, {dados['numero']}, {dados['bairro']}, {dados['municipio']}, {dados['uf']}, CEP: {dados['cep']}")
            print(f"Telefone 1: {dados.get('ddd_telefone_1', 'Não informado')}")
            print(f"Telefone 2: {dados.get('ddd_telefone_2', 'Não informado')}")
            print(f"Email: {dados.get('email', 'Não informado')}")
            print(f"Porte: {dados.get('porte', 'Não informado')}")

            # Exibir informações dos sócios (QSA)
            print("\nQuadro Societário (QSA):")
            for socio in dados.get('qsa', []):
                print(f"Nome do Sócio: {socio['nome_socio']}")
                print(f"Faixa Etária: {socio['faixa_etaria']}")
                print(f"Qualificação: {socio['qualificacao_socio']}")
                print()
        else:
            print("Erro na requisição. Verifique o CNPJ e tente novamente.\n")


def menu():
    while True:
        print("Escolha uma opção:")
        print("1 - Buscar por CEP")
        print("2 - Buscar por CNPJ")
        print("3 - Sair")

        escolha = input("Digite o número da opção desejada: ")

        if escolha == '1':
            buscar_cep()
        elif escolha == '2':
            buscar_cnpj()
        elif escolha == '3':
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.\n")


# Chamar a função principal do menu
menu()
