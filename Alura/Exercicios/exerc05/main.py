from modelos.app01 import Restaurante
from modelos.app02 import Carro, Cleinte
def exerc01():
    restaurante_praca = Restaurante('praca', 'italiana')
    restaurante_pizza = Restaurante('Pizza Place', 'Fast Food')

    restaurante_pizza.troca_estado()

    restaurante_pizza.mostrar_restaurantes()

def exerc02():
    camaro = Carro('camaro', 'amarelo', 2020 )
    jogador01 = Cleinte('Matheus', 'Oparios', 3000, 'Reino Negro')
    jogador02 = Cleinte('Mathaiuos', 'Carmesim', 20, 'Impero dos Tres aneis')
    jogador03 = Cleinte('Matharianos','Olimpiano', 10000, 'Reino Superior de mandala')

def main ():
    exerc01()
    exerc02()


if __name__ == '__main__':
    main()