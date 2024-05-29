class Musica:

    def __init__(self, nome, artista, tempo):

        self.nome_musica = nome
        self.artista = artista
        self.duracao_musica = tempo

    def __str__(self):
        return f'Musica : {self.nome_musica}\n Artista:{self.artista}'

musica1 = Musica('NewDivied', 'linkinPark', 222)
musica2 = Musica('RobLucci', 'Markim', 465)

print(musica1)
print('*'*10)
print(musica2)
