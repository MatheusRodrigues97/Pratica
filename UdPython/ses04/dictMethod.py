pessoa = {"nome": "Matheus Rodrigues", "sobrenome": "Santa Rosa da Cunha"}

print(pessoa.__len__())

for itens, valores in pessoa.items():
    print(f"index :{itens} and valores: {valores}")

d2 = pessoa.copy()