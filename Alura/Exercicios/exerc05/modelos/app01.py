#Reslução de exercicos01

class Restaurante:
    '''
    Classe principal para criação dos objetivos restaurantes na app.
    '''
    
    def __init__(self,nome, categoria):
        '''
        Metodo construtor da classe, obrigado a colocar o nome e categoria do restaurante
        todo novo restaurante estará com status False(inativo), ate ser ativado.
        '''
        
        self._nome = nome 
        self._categoria = categoria
        self._ativo = False

    def __str__(self):
        '''
        Metodo para demostrar o restaurante cadastrado  
        '''
        return f'Restaurante: {self._nome}, tipo:{self._categoria}, status: {self._ativo}'

