import os

lista_restaurantes = []

def exibir_nome_programa():

    print('Sabor Express\n')

def finalizar_app():

    os.system('clear')
    print(f'encerrando app\n')
    

def exibir_opcoes ():

    print('1 cadastrar restaurante')
    print('2 listar restaurante')
    print('3 ativar restaurante')
    print('4 sair\n')

def cadastrar_restaurante():

    os.system('clear')
    
    nome_restaurante = input('Digite o nome do resturante: ')
    lista_restaurantes.append(nome_restaurante)
    print(f'Restaurantes {lista_restaurantes} cadastrado com sucesso')

    opcao_invalida()   


def opcao_invalida():
    
    resposta = input('Digite uma tecla para voltar ao menu principal: ')
    
    if not resposta:
        opcao_invalida()  
    else:
        main()

def listar_restaurantes ():
    
    os.system('clear')
    
    for restaurante in lista_restaurantes:
        print('restaurante {restaurante}')
    
    main()


def escolher_opcao():
    try:
        opcao_escolhida = int(input("Opção escolhida: "))
        print(f'Você escolheu a opção {opcao_escolhida}')

        if opcao_escolhida == 1:
            print(f'cadastre o restaurante')

        elif opcao_escolhida == 2:
            print(f'listando os restaurante cadastrados')

        elif opcao_escolhida == 3:
            print(f'ativar resturantes')

        elif opcao_escolhida == 4:
            finalizar_app()
    
    except:
        opcao_invalida()

def main():
    os.system('clear')
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()