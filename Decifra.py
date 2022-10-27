alfabeto_normal = list("abcdefghijklmnopqrstuvwxyz")

novo_alfabeto = list(input())
frase_criptografada = list(input())
nova_frase = ""

for i in frase_criptografada:
    index = alfabeto_normal.index(i)
    nova_frase += novo_alfabeto[index]

print(nova_frase)