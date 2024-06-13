class Carro:

    def __init__(self, modelo, cor, ano) :
        
        self._modelo = modelo
        self._cor = cor
        self._ano = ano

class Cleinte:

    personagem = []
    def __init__(self, nome, sobrenome, idade, endereco):
        
        self._nome = nome
        self._sobrenome = sobrenome
        self._idade = idade
        self._endereco = endereco
        Cleinte.personagens.append(self)
   
    def __str__(self) -> str:
        return f'Seu nome é {self._nome} e você mora no endereço {self._endereco}'