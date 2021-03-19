# Clico de vida
"""
arquivo = open("texto.doc", "w")
arquivo.write("marcelo amaro")
arquivo.close()

arquivo = open("texto.pfd", "w")
arquivo.write("marcelo amaro")
arquivo.close()

arquivo = open("texto.txt", "w")
arquivo.write("marcelo amaro")
arquivo.close()

arquivo2 = open("numero.txt", "w")

for linha in range(1,10):
    arquivo2.write(f"{linha}\n")
arquivo2.close()

arquivo3 = open("cadastro.txt", "w")
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade:"))
arquivo3.write(f"{nome}\n")
arquivo3.write(f"{idade}\n")
arquivo3.close()

cadastro = open("cadastro.txt", "w") #criação
cadastro.write(input("Nome:"))
cadastro.write(input("Idade:"))

arquivo4 = open("cadrasto,txt", "r")

for linha in arquivo4.readlines():
    print(linha)
arquivo4.close()    

with open("cadrasto.txt", "r")as linha:
    for linha in arquivo4.readlines():
        print(linha)

with open("impares.txt", "w") as impares:
    with open("pares.txt", "w") as pares:
        for n in range(0,100):
            if n % 2 == 0:
                pares.write(f"{n}\n")
        else:
            impares.write(f"{n}\n") 

                       
nomes = open("nomes.txt")

line = nomes.readline()

word = line.strip()

for line in nomes:
    word = line.strip()
    if len(word) <=3:
        print(word)
        
nomes = open("nomes.txt")

for line in nomes.readlines():
    if line[0]=="A":
        print(line.upper())
nomes.close()  

nomes = open("nomes.txt")

for line in nomes.readlines():
    if line[0]=="A" and len(line)<=4:
        print(line.upper())
nomes.close ()    
"""
#HTML
with open("home.html", "w", encoding="utf-8")as home:
    home.write("""
<!DOCTYPE html>
    <html lang="pt-br">
        <head>
            <title>Título da página</title>
            <meta charset="utf-8">
        </head>
    <body>
    
""")
   </body>
</html>