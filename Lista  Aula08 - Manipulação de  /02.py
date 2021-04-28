"""Para esse exercício utilize o arquivo nomes.txt.
    • Leia o arquivo nomes.txt e imprima o tamanho de cada nome
    • Crie um arquivo apenas com nomes iniciados com a letra A
    • Crie um arquivo apenas com palíndromos.
    • Faça a busca por determinado nome dentro do arquivo e retorne True caso ele exista. """

#Leia o arquivo nomes.txt e imprima o tamanho de cada nome
nomes = open("nomes.txt")

line = nomes.readline()

word = line.strip()

for line in nomes:
    word = line.strip()
    if len(word):
        for caractere in word:
            print(caractere, end='')
"""
#Crie um arquivo apenas com nomes iniciados com a letra A
with open("nomes_a.txt", "w") as nomes_a:
    with open("nomes.txt") as line:
        for l in line.readlines():
            if line[0]=="A":
                nomes_a.write(l)
 """               
