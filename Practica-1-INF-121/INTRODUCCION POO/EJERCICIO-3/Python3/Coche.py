#Crea una clase Coche con marca, modelo y velocidad
class Coche:
    def __init__(self,marca,modelo):
        self.marca=marca
        self.modelo = modelo
        self.velocidad= 0

    #a) Agrega un método acelerar () que aumente la velocidad en 10
    def acelerar(self):
        self.velocidad += 10
        print(f"{self.marca} {self.modelo} ha acelerado . Velocidad actual es : {self.velocidad}")
    #b) Agrega un método frenar () que disminuya la velocidad en 5
    def frenar (self):
        self.velocidad -= 5
        if self.velocidad < 0:
            self.velocidad = 0
        print (f"{self.marca} {self.modelo} ha frenado . Velocidad actual : {self.velocidad}")
#Crea dos coches, aceléralos, frénalos y muestra sus velocidades
coche1 = Coche("Toyota","Corolla")
coche2 =Coche ("Ford","Focus")

coche1.acelerar()
coche2.acelerar()

coche1.frenar()
coche2.frenar()

print(f"Velocidad final de {coche1.marca} {coche1.modelo}: {coche1.velocidad} km/h")
print(f"Velocidad final de {coche2.marca} {coche2.modelo}: {coche2.velocidad} km/h")

    



    