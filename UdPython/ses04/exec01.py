def multiplica (*args):

    values = 1

    for numbers in args:
        values = values * numbers 

    
    return f"O Resultado foi {values}"

def recebimento ():

    i = 0
    lista_numeros =[]

    while i < 3:
        
        value_number = int(input(f"digite 10 numeros aleatorios começando{i} : "))  
        lista_numeros.append(value_number)  
        
        i+=1
    
    multiplica(*lista_numeros)

def main ():

    multiplica(1,2,3,4,5,6,7,8,8,9)

main()