from modelos.avaliacao import Avaliador
from modelos.cardapio.item_cardapio import ItemCardapio
class Restaurante:
    restaurantes = []
     
    def __init__(self, nome, categoria ):

        self._nome = nome.title()
        self.categoria = categoria.upper()
        self._ativo = False
        self._avaliador = []
        self._cardapio = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self._nome} | {self.categoria}'
    
    @classmethod
    def listar_restaurantes(cls):
        print(f"{'Nome do restaurante'.ljust(20)} | {'Categoria'.ljust(20)} |{'Avalição'.ljust(20)} | {'Status'}")
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} |{str(restaurante.media_avaliacoes).ljust(25)} |{restaurante.ativo}')
    
    @property
    def ativo(self):
        return 'ativo' if self._ativo else 'desativado'

    def alternar_estado(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        if 0 < nota <= 5:
            avaliacao = Avaliador(cliente, nota)
            self._avaliador.append(avaliacao)

    @property
    def media_avaliacoes(self):
       
        if not self._avaliador:
            return '-' 
        
        soma_das_notas = sum(Avaliador._nota for avaliador in self._avaliador)
        quantidades_notas = len(self._avaliador)
        media = round(soma_das_notas / quantidades_notas, 1)
        
        return media

    def adiconar_cardapio(self, item):
        if isinstance(item, ItemCardapio):
            self._cardapio.append(item)
    
   

    @property
    def exibir_cardapio(self):
        print(f'Cardapio do restaurante {self._nome}\n')
        for i,item in enumerate(self._cardapio,start=1):
                if hasattr(item,'descricao'):
                        mensagem_prato = f'{i}. Nome: {item._nome} | Preço: R${item._preco} | Descrição: {item.descricao}'
                        print(mensagem_prato)
                else:
                        mensagem_bebida = f'{i}. Nome: {item._nome} | Preço: R${item._preco} | Tamanho: {item.tamanho}'
                        print(mensagem_bebida)






