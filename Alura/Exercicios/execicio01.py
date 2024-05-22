#1 -> Cria uma lista para cada informação a seguir
"""
-> Lista de numeros de 1 a 10

-> Lista com quatro nomes

-> Lista com o ano que você nasceu e o ano atual

"""
def listar_numeros(n):
    lista_de_numeros: int = []
    
    lista_de_numeros = adicinar_dados(lista_de_numeros, n)
    print(f'Lista {lista_de_numeros}')

def listar_nomes(n):
    lista_de_nomes: str = [] 
    
    lista_de_nomes = adicinar_dados(lista_de_nomes, n)   
    print(f'Nomes {lista_de_nomes}')

def listar_ano_nascimento(n):
    lista_ano_nascimento: int = []

    lista_ano_nascimento = adicinar_dados(lista_ano_nascimento, n)
####################################################################################

def adicinar_dados(lista ,tamanho):
    i = 0

    while i < tamanho:
        try:
            valor = input('Digite um valor')
            lista.append(valor)
           
            i+=1

        except TypeError:
            print('Tipo de valor invalido para lista')
         
    return lista






def main():
    listar_numeros(10)
    listar_nomes(5)
    listar_ano_nascimento(5)

main()      


