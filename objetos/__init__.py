from interface import cabecalho, linha, menu
from random import randint


class Arquivo:
    def __init__(self, nome_arquivo):
        self.nome_arquivo = nome_arquivo

    def arquivo_existe(self):
        try:
            a = open(self.nome_arquivo, 'rt')
            a.close()
        except FileNotFoundError:
            return False
        else:
            return True

    def criar_arquivo(self):
        try:
            a = open(self.nome_arquivo, 'wt+')
            a.close()
        except:
            print('\033[31mHouve um ERRO na criação do arquivo\033[m')
        else:
            print(f'\033[33mArquivo {self.nome_arquivo} criado com sucesso.\033[m')

    def ler_arquivo(self):
        global a
        try:
            a = open(self.nome_arquivo, 'rt')
        except:
            print('\033[31mERRO ao ler arquivo.\033[m')
        else:
            if self.nome_arquivo == 'clientes.txt':
                c = 0
                cabecalho(f'Arquivo {self.nome_arquivo}')
                for linha in a:
                    dado = linha.split(';')
                    dado[2] = dado[2].replace('\n', '')
                    print(f'{c} - ID:{dado[0]}{dado[1]:^30}{dado[2]:>3} anos')
                    c += 1
            elif self.nome_arquivo == 'veiculos.txt':
                c = 0
                cabecalho(f'Arquivo {self.nome_arquivo}')
                for linha in a:
                    dado = linha.split(';')
                    dado[2] = dado[2].replace('\n', '')
                    print(f'{c} - ID:{dado[0]}{dado[1]:^30}{dado[2]:>3}')
                    c += 1

            elif self.nome_arquivo == 'temp.txt':
                c = 0
                cabecalho(f'Arquivo {self.nome_arquivo}')
                for linha in a:
                    dado = linha.split(';')
                    dado[3] = dado[3].replace('\n', '')
                    print(f'{c} - ID:{dado[0]}{dado[1]:^30}{dado[2]:^30}{dado[3]:>3}')
                    c += 1

            elif self.nome_arquivo == 'vendas.txt':
                cabecalho(f'Arquivo {self.nome_arquivo}')
                print(f'{"=" * 20} Vendas {"=" * 20}'.center(50))
                c = 1
                for linha in a:
                    dado = linha.split(';')
                    dado[5] = dado[5].replace('\n', '')
                    print(f'Venda:')
                    print(f'{c} - Cliente:\n\t{dado[0]}{dado[1]:^10}\n\tVeículo: {dado[4]}\t{dado[5]:^10}')
                    print('~' * 50)
                    c += 1
        finally:
            a.close()

    def menu_cadastro_cli(self):
        print(linha())
        resposta = menu('Cadastro de Clientes', ['Cadastrar Novo', 'Remover Cliente', 'Voltar'])

        if resposta == 1:
            Cliente.__id = randint(1, 1000)
            Cliente.__nome = input(f'Digite o nome do cliente: ')
            Cliente.__idade = int(input(f'Digite a idade do cliente: '))
            cliente = Cliente(Cliente.__id, Cliente.__nome, Cliente.__idade)
            Cliente.cadastrar_cliente(cliente)

        elif resposta == 2:
            self.apagar_item()

        elif resposta == 3:
            return

    def menu_cadastro_vei(self):
        print(linha())
        resposta = menu('Cadastro de Veiculo', ['Cadastrar Novo', 'Remover Veículo', 'Voltar'])

        if resposta == 1:
            Veiculo.__id = randint(1001, 2000)
            Veiculo.__marca = input(f'Digite a Marca: ')
            Veiculo.__placa = input(f'Digite a placa: ')
            veiculo = Veiculo(Veiculo.__id, Veiculo.__marca, Veiculo.__placa)
            Veiculo.cadastrar_veiculo(veiculo)

        if resposta == 2:
            self.apagar_item()

        if resposta == 3:
            return

    def apagar_item(self):
        id = False
        try:
            while True:
                excluir = input(f'Que ID deseja excluir? ')
                if not excluir.isnumeric():
                    print('\033[31mERRO! Não é um número.\033[m')
                elif excluir == '0':
                    break
                with open(self.nome_arquivo, 'r') as ex:
                    linhas = ex.readlines()
                    for i in linhas:
                        if i.split(';')[0] == excluir:
                            id = True
                if id == True:
                    print(f'ID{excluir} encontrado.')
                    id = False
                    break
                else:
                    print('\033[31mID não existe\033[m')

            sure = input(f'Tem certeza que deseja \033[31mexcluir ID\033[m {excluir} \033[31m[s]\033[m[n]? ').lower()
            if sure == 'n':
                return
            with open(self.nome_arquivo, 'r+') as f:
                linhas = f.readlines()
                f.seek(0)
                for l in linhas:
                    if excluir not in l:
                        f.write(l)
                    else:
                        print('Item excluído com sucesso.')
                f.truncate()

                if not sure == 'n':
                    print('Solicitação realizada com sucesso')
                    print()
                else:
                    return
        except:
            print('\033[31mERRO! Esse ID não existe.\033[m')

    def registra_venda(self):
        global veiculo
        id = False
        while True:
            cliente = input('Digite o ID do comprador [0] para cancelar: ')
            if cliente == '0':
                break
            with open('clientes.txt', 'r') as cli:
                linhas = cli.readlines()
                for i in linhas:
                    if i.split(';')[0] == cliente:
                        id = True
            if id == True:
                print('Cliente adicionado na Nota de Compra.')
                id = False
                break
            else:
                print("ID não existe.")

        while True:
            if cliente == '0':
                break
            veiculo = input('Digite o ID do veículo [0] para cancelar: ')
            if veiculo == '0':
                break
            with open('veiculos.txt', 'r') as vei:
                linhas = vei.readlines()
                for i in linhas:
                    if i.split(';')[0] == veiculo:
                        id = True
            if id == True:
                print('Veículo adicionado na Nota de Compra.')
                id = False
                break
            else:
                print("ID não existe.")
        try:
            if cliente == '0':
                return
            if veiculo == '0':
                return
            # Copia os dados do cliente comprador pro arquivo temp
            with open('clientes.txt', 'r') as comprador_file:
                linhas = comprador_file.readlines()
                comprador_file.seek(0)
                with open('temp.txt', 'a') as temp:
                    for l in linhas:
                        if cliente in l:
                            temp.write(f'{l};'.replace('\n', ''))

            # Copia os dados da Motoclicleta pro arquivo temp
            with open('veiculos.txt', 'r+') as veiculos_file:
                linhas = veiculos_file.readlines()
                veiculos_file.seek(0)
                with open('temp.txt', 'a') as temp:
                    for l in linhas:
                        if veiculo in l:
                            temp.write(l)
                    temp.truncate()

                # apaga veículo comprado do cadastro
                veiculos_file.seek(0)
                for l in linhas:
                    if veiculo not in l:
                        veiculos_file.write(l)
                    else:
                        print('Item excluído com sucesso.')

                veiculos_file.truncate()

            # grava o arquivo temporário em Vendas
            with open(self.nome_arquivo, 'r') as temp:
                linhas = temp.readlines()
                temp.seek(0)
                with open('vendas.txt', 'a') as vendas:
                    for l in linhas:
                        vendas.write(l)

        except:
            print('\033[31mERRO ao registrar venda.\033[m')
        else:
            print('Venda registrada.')
        # apaga arquivo temporário
        a = open(self.nome_arquivo, 'w+')
        a.close()

    def listar_venda(self):
        try:
            listar = int(input('Listar detalhes da venda por número: '))
            with open('vendas.txt', 'r') as vendas:
                linhas = vendas.readlines()
                det_compra = linhas[listar-1].split(';')
                det_compra[5].replace('\n', '')
                print('~'*50)
                print(f'\033[33mA compra {listar} foi realizada por \033[34m{det_compra[1]}\033[33m'
                      f'\nO veículo é uma \033[34m{det_compra[4]}\033[33m com placa \033[34m{det_compra[5]}\033[33m'
                      f'Agradecemos pela compra. Esperamos vê-lo novamente.\033[m')
                input('Pressione ENTER para continuar')
        except:
            print('\033[31mVocê não escolheu uma venda válida\033[m')

class Cliente(Arquivo):
    def __init__(self, id, nome, idade, nome_arquivo='clientes.txt'):
        super().__init__(nome_arquivo)
        self.__id = id
        self.__nome = nome
        self.__idade = idade

    @property
    def id(self):
        return self.__id

    @property
    def nome(self):
        return self.__nome

    @property
    def idade(self):
        return self.__idade

    @id.setter
    def id(self, id):
        self.__id = id

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @idade.setter
    def idade(self, idade):
        self.__idade = idade

    def compra(self, veiculo):
        pass

    def cadastrar_cliente(self):
        try:
            a = open(self.nome_arquivo, 'at')
        except:
            print('Houve um ERRO ao abrir o arquivo.')
        else:
            try:
                a.write(f'{self.__id};{self.__nome};{self.__idade}\n')
            except:
                print('Houve um ERRO ao escrever no arquivo.')
            else:
                print(f'Novo registro de {self.__nome} adicionado.')
            finally:
                a.close()


class Veiculo(Arquivo):
    def __init__(self, id, marca, placa, nome_arquivo='veiculos.txt'):
        super().__init__(nome_arquivo)
        self.__id = id
        self.__marca = marca
        self.__placa = placa

    @property
    def id(self):
        return self.__id

    @property
    def marca(self):
        return self.__marca

    @property
    def placa(self):
        return self.__placa

    @id.setter
    def id(self, id):
        self.__id = id

    @marca.setter
    def marca(self, marca):
        self.__marca = marca

    @placa.setter
    def placa(self, placa):
        self.__placa = placa

    def cadastrar_veiculo(self):
        try:
            a = open(self.nome_arquivo, 'at')
        except:
            print('Houve um ERRO ao abrir o arquivo.')
        else:
            try:
                a.write(f'{self.__id};{self.__marca};{self.__placa}\n')
            except:
                print('Houve um ERRO ao escrever no arquivo.')
            else:
                print(f'Novo registro do veículo ID:{self.__id} foi adicionado.')
            finally:
                a.close()
