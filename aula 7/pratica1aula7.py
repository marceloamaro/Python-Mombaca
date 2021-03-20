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

#HTML
with open("index.html", "w", encoding="utf-8") as index:
    index.write("""
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
       <meta charset= "utf-8">
       <title>Titulo da Página</title>
    <head>
    <body>
    Olá!
    </body>
    </html>
    """)
    """
filmes = { "drama":["Cidadão Kane", "O Poderoso Chefão"],
 "comedia":["Tempos Modernos", "Desejo de Matar"],
  "ficção":["Ad Astra", "Interestelar"],
   "guerra" : ["1937", "Platoon", "Lágrimas do Sol"] }

with open("filmes.html", "w", encoding="utf-8") as filme:
    filme.write("""
<!DOCTYPE html>
    <html lang="pt-BR">
    <head>
       <meta charset= "utf-8">
       <title>Filmes</title>
    <head>
    <body>

    <h1 align="center"> Filmes</h1>
         """)

    for c, v in filmes.items():
        filme.write(f"<h1>{c}</1h>\n") 
        for e in v:
            filme.write(f"<h3>{e}</h3>\n")
    filme.write("</body></html>")