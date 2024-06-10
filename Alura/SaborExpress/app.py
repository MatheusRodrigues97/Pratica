from modelos.restaurantes import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato
from modelos.cardapio.sobremesa import Sobremesa

restaurante_praca = Restaurante('praca', 'gourmet')
bebida_suco = Bebida('Suco de laranja', 7.00, 'grande')
prato_paozinho = Prato('Pão Frances', 0.50, 'O melhor pao da cidade')
torta_morango = Sobremesa('Torta de morango', 12.50, 'Doce', 'Médio')

bebida_suco.aplicar_desconto()
prato_paozinho.aplicar_desconto()

restaurante_praca.adiconar_cardapio(bebida_suco)
restaurante_praca.adiconar_cardapio(prato_paozinho)
restaurante_praca.adiconar_cardapio(torta_morango)

def main ():
    restaurante_praca.exibir_cardapio


if __name__ == '__main__':
    main()
