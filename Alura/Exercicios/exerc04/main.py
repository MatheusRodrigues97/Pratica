PESSOA = {'nome':'' , 'idade': '', 'cidade':'' }

def cadastrar_pessoa(modelo):
    '''Função onde vai cadastrar a pessoa usando o dicionario como modelo'''
    if not modelo['nome']:
        print('Erro de dicionario')
    else:
        nome_pessoa = input('Digite o nome da pessoa :')
        idade_pessoa = int(input(f'Digite a idade {nome_pessoa} :'))
        cidade_pessoa = input(f'Digite a cidade onde {nome_pessoa} vive :')

    modelo['nome'] = nome_pessoa
    modelo['idade'] = idade_pessoa
    modelo['cidade']= cidade_pessoa

    modelo = editar_pessoa(modelo)

    return modelo  

def mensagem(value):
    '''Funão para imprimir se codigo foi um sucesso '''
    print(f'cadastrado com sucesso {value}')

def editar_pessoa(dic_pessoa):
    
    adicionar_profissao = input('Digite a profissão da pessoa :')

    dic_pessoa.update({'profissão': adicionar_profissao})
    
    del dic_pessoa['idade']

    return dic_pessoa


def main():
    
    pessoa_cadastro =  cadastrar_pessoa(PESSOA)
    mensagem(pessoa_cadastro)
    

main()