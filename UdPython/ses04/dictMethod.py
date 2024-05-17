def pega_valor ():
    
    adivinha = input("Escreva um nome de um objeto para que possa adivinhar : ")
    
    if not adivinha:
        raise("Digite um objetivo")
    
    valor = set(adivinha)
    return valor

def main ():
    letras = pega_valor()
    
    print (f"Letras em ordem doidas {letras}")

main()