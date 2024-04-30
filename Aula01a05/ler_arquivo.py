arq = open('arquivo.txt', 'r')

read = arq.read()
lista_nova = []
for line in read:
    if line[:-1] == '\n':
        lista_nova.append(line[:-1])
    else:
        lista_nova.append(line)

print(lista_nova)