#Reslução de exercicos01

class Restaurante:
    '''
    Classe principal para criação dos objetivos restaurantes na app.
    '''
    res = []
    def __init__(self,nome, categoria):
        '''
        Metodo construtor da classe, obrigado a colocar o nome e categoria do restaurante
        todo novo restaurante estará com status False(inativo), ate ser ativado.
        '''
        
        self._nome = nome 
        self._categoria = categoria
        self._ativo = False
        Restaurante.res.append(self)


    def __str__(self):
        '''
        Metodo para demostrar o restaurante cadastrado  
        '''
        return f'Restaurante: {self._nome}, tipo:{self._categoria}'
    
    @classmethod
    def mostrar_restaurantes(cls):
        '''
        Metodo da classe para listar todos os restaurantes cadastrados e seus status
        '''
        for restaurante in cls.res:
             print (f'\nRestaurante: {restaurante._nome}\n | Categoria: {restaurante._categoria} \n| Status: {restaurante.ativo}')

    @property
    def ativo(self):
        '''
        Propriedade para verificar se o restaurante esta ativo 
        '''
        return 'ativo' if self._ativo else 'desativado'
    
    def troca_estado(self):
        self._ativo = not self._ativo
