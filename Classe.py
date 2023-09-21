#Classe
class carro ():
    #Atributos da classe
    marca = str()
    cor_carro = str()
    portas = int()
    lugares = int()
    vidro_eletrico = bool()

#Metódo contrutor
    def __init__ (self,marca,cor,portas,lugares,vidro_eletrico):
        #Atributos de Instancia
        self.marca = marca
        self.cor_carro = cor
        self.portas = portas
        self.lugares = lugares
        self.vidro_eletrico = vidro_eletrico
        print("O Carro foi criado")
        

a1 = carro("Fiat","vermelho",2,4,True)

# Listar informações de a1
for atributo in dir(a1):
    # Exclua atributos especiais e métodos internos
    if not atributo.startswith("__"):
        print(atributo, getattr(a1, atributo))