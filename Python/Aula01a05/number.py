try:
    x = int(input(" Qual valor de x ?"))
    

except ValueError:
    print("Digite um numero ")
else:
    print(f"x is {x}")