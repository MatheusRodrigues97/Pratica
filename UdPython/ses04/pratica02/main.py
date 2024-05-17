def pegar_valor():
    
    print("Programa para multiplicar e somar uma sequencia numerica")
    
    multiplicador = int(input("digite um multiplicador entre 1 a 10: "))
    
    lista_numeros = [] 
    
    i = 0
    while i < (multiplicador*2) :
        
        value = int(input("Digite um numero inteiro: "))

        lista_numeros.append(value)

        i+=1
    

    return lista_numeros, multiplicador



def main ():
    
    lista_numeros, multiplicador = pegar_valor()

    soma = sum( multiplicador * value for value in lista_numeros)

    

    print(f"sua lista de numeros {lista_numeros} e seu multiplicador {multiplicador} resultado final é {soma}")

main()
