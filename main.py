from interface import *
from objetos import Arquivo

temp = Arquivo('temp.txt')
if not Arquivo.arquivo_existe(temp):
    Arquivo.criar_arquivo(temp)

clientes = Arquivo('clientes.txt')
if not Arquivo.arquivo_existe(clientes):
    Arquivo.criar_arquivo(clientes)

veiculos = Arquivo('veiculos.txt')
if not Arquivo.arquivo_existe(veiculos):
    Arquivo.criar_arquivo(veiculos)

vendas = Arquivo('vendas.txt')
if not Arquivo.arquivo_existe(vendas):
    Arquivo.criar_arquivo(vendas)

cabecalho('Cadastro de Vendas')

while True:

    resposta = menu('Menu Principal', ['Listar Clientes', 'Cadastrar Cliente', 'Listar Veículos',
                                       'Cadastrar Veículo', 'Registrar Venda', 'Listar Vendas', 'Sair'])

    if resposta == 1:
        Arquivo.ler_arquivo(clientes)

    elif resposta == 2:
        Arquivo.menu_cadastro_cli(clientes)

    elif resposta == 3:
        Arquivo.ler_arquivo(veiculos)

    elif resposta == 4:
        Arquivo.menu_cadastro_vei(veiculos)

    elif resposta == 5:
        Arquivo.registra_venda(temp)

    elif resposta == 6:
        Arquivo.ler_arquivo(vendas)
        venda = Arquivo.listar_venda(vendas)

    elif resposta == 7:
        print('VOLTE SEMPRE!!')
        break
