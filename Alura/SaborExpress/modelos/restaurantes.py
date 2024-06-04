from modelos.avaliacao import Avaliador
class Restaurante:
    restaurantes = []
     
    def __init__(self, nome, categoria ):

        self._nome = nome.title()
        self.categoria = categoria.upper()
        self._ativo = False
        self._avaliador = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self._nome} | {self.categoria}'
    
    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} |{'Status'}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} |{str(restaurante.media_avaliacoes).ljust(25)} |{restaurante.ativo}')
    
    @property
    def ativo(self):
        return 'ativo' if self._ativo else 'desativado'

    def alternar_estado(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        
        avaliacao = Avaliador(cliente, nota)
        self._avaliador.append(avaliacao)

    @property
    def media_avaliacoes(self):
       
        if not self._avaliador:
            return 0 
        
        soma_das_notas = sum(Avaliador._nota for avaliador in self._avaliador)
        quantidades_notas = len(self._avaliador)
        media = round(soma_das_notas / quantidades_notas, 1)
        
        return media




