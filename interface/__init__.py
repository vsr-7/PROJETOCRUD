def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! Por favor, digite um número inteiro válido!\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mERRO! Usuário preferiu não digitar um número.\033[m')
            return
        else:
            return n


def linha(obj='\U0001f3ce\uFE0F', tam=50):
    return (obj * tam)


def cabecalho(txt):
    print(linha())
    print(txt.center(50))
    print(linha())


def menu(msg, lista):
    cabecalho(f'\033[33m\t{msg}\033[m')
    c = 1
    for item in lista:
        print(f'\033[33m{c} -\t\033[m \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('\033[33mSua Opção: \033[m')
    return opc
