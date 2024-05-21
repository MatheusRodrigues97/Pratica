import os

print('Sabor Express\n')

print('1 cadastrar restaurante')
print('2 listar restaurante')
print('3 ativar restaurante')
print('4 sair\n')

opcao_escolhida = int(input("Opção escolhida: "))
print(f'Você escolheu a opção {opcao_escolhida}')

def finalizar_app():
    os.system('clear')
    print(f'encerrando app\n')
    

if opcao_escolhida == 1:
    print(f'cadastre o restaurante')

elif opcao_escolhida == 2:
    print(f'listando os restaurante cadastrados')

elif opcao_escolhida == 3:
    print(f'ativar resturantes')

else:
    finalizar_app()