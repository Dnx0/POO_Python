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

#Classe Derivada
class modelo (carro):
    modelo = str()
    ano = int()
    placa = str()
    #Metodo construtor das instancias
    def __init__ (self,marca,cor,portas,lugares,vidro_eletrico,modelo,ano,placa):
        #Pega os atributos da classe pai, da classe acima com super()
        super().__init__(marca,cor,portas,lugares,vidro_eletrico)
        self.modelo = modelo
        self.ano = ano
        self.placa = placa
    
    #Função para analisar todos as informarções de uma instancia
    def info_geral (self):
        print("""Informações gerias->
        Nome do carro : {0}
        Ano do carro : {1}
        Placa do carro: {2}
        Fabricante: {3}
        Cor do carro: {4}
        Número de portas: {5}
        Número de lugares: {6}
        Vidro eletrico: {7}
        """.format(self.modelo,self.ano,self.placa,self.marca,self.cor_carro,self.portas,self.lugares,self.vidro_eletrico))


a1 = carro("Fiat","vermelho",2,4,True)
a2 = modelo("Ford","Azul",4,5,True,"Fiesta",2015,"fal6915")

a2.info_geral()
"""
# Listar informações de a1
for atributo in dir(a1):
    # Exclua atributos especiais e métodos internos
    if not atributo.startswith("__"):
        print(atributo, getattr(a1, atributo))
"""