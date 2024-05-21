class Pessoa():
    def __init__(self, nome, idade, peso):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.comendo = False
        self.dormindo = False
        self.falando = False
    def comer (self, comida="", bebida =""):
        if self.dormindo == True:
            print(f"{self.nome} não pode comer, está tentando dormir!")
        elif self.falando == True:
            print(f"{self.nome} não pode comer, está falando!")
        elif comida == "" and bebida == "":
            print(f"{self.nome} não está comendo nem bebendo nada")
        elif comida == "" and bebida !="":
            print(f"{self.nome} não está comendo, só bebendo {bebida}")
            self.comendo = True
        elif comida != "" and bebida == "":
            print(f"{self.nome} está comendo{comida} mas não está bebendo nada")
            self.comendo = True
        elif comida != "" and bebida != "":
            print(f"{self.nome} está comendo {comida} e bebendo {bebida}")
            self.comendo = True
    def dormindo (self):
        if self.comendo == True:
            print(f"{self.nome} não pode dormir, está comendo")
        elif self.falando == True:
            print(f"{self.nome} não pode dormir, está falando")
        elif self.dormindo == True:
            print(f"{self.nome} já está dormindo")
    def falando (self, falar = ""):
        if self.comendo == True:
            print(f"{self.nome} está comendo e não pode falar")
        elif self.dormindo == True:
            print(f"{self.nome} está dormindo e não pode falar")
        elif falar == "":
            print(f"{self.nome} não está falando")
        elif falar != "":
            print(f"{self.nome} está falando {falar}")
            self.falando = True
#ordem para finalizar ações:
    def finalfalar (self):
        if self.falando == True:
            self.falando = False
        else:
            self.falando = False
            print(f"{self.nome} Se calou")
    def finaldormindo (self):
        if self.dormindo == True:
            self.dormindo = False
        else:
            self.dormindo = False
            print(f"{self.nome} já está acordado")
    def finalcomer (self):
        if self.comendo == True:
            self.comendo = False
            print(f"{self.nome} parou de comer")
        else:
            self.comendo = False
            print(f"Já está sem comer")