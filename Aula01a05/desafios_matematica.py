import random

OPERACAOES = ["+", "-","*","/"]
MIN_OPERACOES = 3
MAX_OPERACOES = 12

def gerar_problema ():
    left = random.randint(MIN_OPERACOES, MAX_OPERACOES)
    right = random.randint(MIN_OPERACOES, MAX_OPERACOES)
    operador = random.choice(OPERACAOES)

    exper = str(left)+ " " + operador + " " + str (right) 
    resultado = eval(exper)
    return exper, resultado

exper, resultado = gerar_problema()

print(exper, " = ",resultado)



