from modelos.app01 import Restaurante

def main ():
    restaurante_praca = Restaurante('praca', 'italiana')
    restaurante_pizza = Restaurante('Pizza Place', 'Fast Food')

    restaurante_pizza.troca_estado()

    restaurante_pizza.mostrar_restaurantes()


if __name__ == '__main__':
    main()