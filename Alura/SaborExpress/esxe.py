import os

lista_restaurantes = [{'nome': 'Praça', 'categoria': 'Japones', 'ativo': False},
                      {'nome': 'Pizza suprema', 'categoria': 'italina', 'ativo': True},
                      {'nome': 'CantinaDaVó', 'categoria':'italiano', 'ativo':False}]

def exibir_nome_programa():

    print('Sabor Express\n')

def finalizar_app():
    '''Função que encerrar o execução do aplicativo '''

    os.system('clear')
    print(f'encerrando app\n')
    

def exibir_opcoes ():
    '''Função para exibir o menu do programa a pessoa '''

    print('1 cadastrar restaurante')
    print('2 listar restaurante')
    print('3 Alternar estado do restaurante')
    print('4 sair\n')

def cadastrar_restaurante():
    '''Função responsavel por cadastrar um restaurante no dicionario modelo'''

    os.system('clear')
    print(f'Cadastre o seu restaurante\n')
    
    nome_restaurante = input('Digite o nome do resturante: ')
    categoria = input(f'\nDigite a categoria do resturante {nome_restaurante} :')

    novo_restaurante = {'nome': nome_restaurante, 'categoria': categoria, 'ativo': False}
    lista_restaurantes.append(novo_restaurante)

    opcao_invalida()   


def opcao_invalida():
    '''Função responsavel para retornar ao menu principal do programa'''
    resposta = input('Digite uma tecla para voltar ao menu principal: ')
    
    if not resposta:
        opcao_invalida()  
    else:
        main()

def listar_restaurantes():
    '''Função que vai listar os restaurantes e seus dados cadastrados no dicionario '''

    os.system('clear')

    print(f'listando os restaurante cadastrados')
    
    for restaurante in lista_restaurantes:

        nome_restaurante = restaurante['nome']
        categoria_restaurante = restaurante['categoria']
        ativo = f'ativo' if restaurante['ativo'] == True else f'desativado'
        
        print(f'\nrestaurante  = {nome_restaurante.ljust(20)} | tipo = {categoria_restaurante.ljust(20)} | Ativo = {ativo.ljust(20)}\n')
    opcao_invalida() 
    
def alternar_estado_restaurante():
    '''Função que vai alterar o status do restaurante '''

    os.system('clear')
    
    print('Alterar o estado do restaurante')

    nome_restaurante = input('Digite o nome do restaurante para alterar o estado: ')
    restaurante_encontrado = False

    for restaurante in lista_restaurantes:
        if nome_restaurante == restaurante['nome']:
            
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante { nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante}, foi desativado com sucesso '
            print(mensagem)

    if not restaurante_encontrado:
        print('O restaurante não foi encotrado ')
    
    opcao_invalida()

def escolher_opcao():
    '''Função reponsavel pelas chamadas das funções de acordo com o numero da opção escolhida'''
    
    try:
        opcao_escolhida = int(input("Opção escolhida: "))
        print(f'Você escolheu a opção {opcao_escolhida}')

        if opcao_escolhida == 1:
            cadastrar_restaurante()

        elif opcao_escolhida == 2:
            listar_restaurantes()

        elif opcao_escolhida == 3:
            alternar_estado_restaurante()

        elif opcao_escolhida == 4:
            finalizar_app()
    
    except:
        opcao_invalida()

def main():
    '''Função principal de inicialização do programa'''

    os.system('clear')
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()