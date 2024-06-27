from django.db import models

class Fotografia(models.Model):
    '''
    Classe modelo ORM para o banco de dados herdando o modelo da model para usar nas imagens do site
    '''

    OPCOES_CATEGORIA = [
        ("NEBULOSA","Nebulosa"),
        ("ESTRELA","Estrela"),
        ("GALÁXIA","Galáxia"),
        ("PLANETA","Planeta"),
    ]    
    
    nome = models.CharField(max_length = 100, null = False, blank = False)
    legenda = models.CharField(max_length = 150, null = False, blank = False)
    categoria = models.CharField(max_length=100, choices= OPCOES_CATEGORIA, default='')
    descricao = models.TextField(null= False, blank= False)
    foto = models.CharField(max_length = 100, null = False, blank = False)
    publicada = models.BooleanField(default= False)

    def __str__(self) -> str:
        return f'Fotografia [nome = {self.nome}]'