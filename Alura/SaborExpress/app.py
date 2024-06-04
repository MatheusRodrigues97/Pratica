from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praça', 'gourmet')
restaurante_mexicano = Restaurante('Mexican_food', 'Mexicana')

def main ():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()
