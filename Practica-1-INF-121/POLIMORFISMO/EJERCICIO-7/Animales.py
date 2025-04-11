#Se hace referencia a algunos animales mediante las siguientes clases: La clase Perro con nombre, edad y raza. La clase Gato con nombre y color. La clase Pajaro con nombre y tipo
#a) Instanciar 1 Perro, 1 Gato y 1 Pájaro.
#b) Sobrecargar el método hacerSonido() para que cada animal emita su sonido característico.
#c) Implementar un método moverse() que indique cómo se mueve cada animal (correr, saltar, volar, etc.).
class Perro:
    def __init__(self, nombre, edad, raza):
        self.nombre = nombre
        self.edad = edad
        self.raza = raza

    def hacer_sonido(self):
        return "¡Guau!"

    def moverse(self):
        return "corre"

    def mostrar_info(self):
        print(f"Perro: {self.nombre}, Edad: {self.edad}, Raza: {self.raza}")
        print(f"Sonido: {self.hacer_sonido()}")
        print(f"Se mueve: {self.moverse()}")


class Gato:
    def __init__(self, nombre, color):
        self.nombre = nombre
        self.color = color

    def hacer_sonido(self):
        return "¡Miau!"

    def moverse(self):
        return "salta"

    def mostrar_info(self):
        print(f"Gato: {self.nombre}, Color: {self.color}")
        print(f"Sonido: {self.hacer_sonido()}")
        print(f"Se mueve: {self.moverse()}")


class Pajaro:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo

    def hacer_sonido(self):
        return "¡Pío!"

    def moverse(self):
        return "vuela"

    def mostrar_info(self):
        print(f"Pájaro: {self.nombre}, Tipo: {self.tipo}")
        print(f"Sonido: {self.hacer_sonido()}")
        print(f"Se mueve: {self.moverse()}")


def Animales():
    
    perro1 = Perro("Rex", 5, "Labrador")
    gato1 = Gato("Miau", "Gris")
    pajaro1 = Pajaro("Tweety", "Canario")

    
    print("Información del Perro:")
    perro1.mostrar_info()
    print()

    print("Información del Gato:")
    gato1.mostrar_info()
    print()

    print("Información del Pájaro:")
    pajaro1.mostrar_info()


if __name__ == "__main__":
    Animales()