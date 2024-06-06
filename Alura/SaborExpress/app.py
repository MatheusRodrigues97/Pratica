from modelos.restaurantes import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_praca = Restaurante('praca', 'gourmet')
bebida_suco = Bebida('Suco de laranja', 7.00, 'grande')
prato_paozinho = Prato('Pão Frances', 0.50, 'O melhor pao da cidade')

def main ():
    print(bebida_suco)
    print(prato_paozinho)


if __name__ == '__main__':
    main()
