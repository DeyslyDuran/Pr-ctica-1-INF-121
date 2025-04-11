#Para los bloques del juego Minecraft se usará los siguientes objetos:
#La clase BloqueCofre con capacidad,resistencia y tipo. La clase BloqueTnt con tipo y daño. La clase BloqueHomo con color y capacidadComida 
#a) Crear e instanciar al menos 2 bloques de cada tipo 
#b) Sobrescribe accion() en BloqueCofre, BloqueTnt y BloqueHorno, mostrando distintos mensajes según el tipo de bloque.
#c) Sobrecarga colocar() para permitir colocar un bloque en diferentes orientaciones (por ejemplo, en el suelo o en la pared).
#d) Sobrescribe romper() en BloqueCofre, BloqueTnt y BloqueHorno, mostrando distintos mensajes según el tipo de bloque y que puede suceder al romperlos.

class BloqueCofre:
    def __init__(self, capacidad, resistencia, tipo):
        self.capacidad = capacidad
        self.resistencia = resistencia
        self.tipo = tipo

    def accion(self):
        return f"Abriendo el cofre de tipo {self.tipo}."

    def colocar(self, orientacion):
        return f"Colocando el cofre en posición {orientacion}."

    def romper(self):
        return f"Rompiendo el cofre de tipo {self.tipo}. Puede que se derramen los objetos dentro."


class BloqueTnt:
    def __init__(self, tipo, daño):
        self.tipo = tipo
        self.daño = daño

    def accion(self):
        return f"Activando el TNT de tipo {self.tipo}."

    def colocar(self, orientacion):
        return f"Colocando el TNT en posición {orientacion}."

    def romper(self):
        return f"Rompiendo el TNT de tipo {self.tipo}. ¡Cuidado! Puede explotar."


class BloqueHorno:
    def __init__(self, color, capacidad_comida):
        self.color = color
        self.capacidad_comida = capacidad_comida

    def accion(self):
        return f"Usando el horno de color {self.color}."

    def colocar(self, orientacion):
        return f"Colocando el horno en posición {orientacion}."

    def romper(self):
        return f"Rompiendo el horno de color {self.color}. Puede que se rompa y se pierda comida."


def main():
    # Instanciar 2 bloques de cada tipo
    cofre1 = BloqueCofre(capacidad=27, resistencia=5, tipo="Madera")
    cofre2 = BloqueCofre(capacidad=54, resistencia=10, tipo="Metal")

    tnt1 = BloqueTnt(tipo="TNT Normal", daño=100)
    tnt2 = BloqueTnt(tipo="TNT Especial", daño=200)

    horno1 = BloqueHorno(color="Gris", capacidad_comida=10)
    horno2 = BloqueHorno(color="Negro", capacidad_comida=15)

    # Mostrar acciones y colocaciones
    print(cofre1.accion())
    print(cofre1.colocar("suelo"))
    print(cofre1.romper())
    print()

    print(cofre2.accion())
    print(cofre2.colocar("pared"))
    print(cofre2.romper())
    print()

    print(tnt1.accion())
    print(tnt1.colocar("suelo"))
    print(tnt1.romper())
    print()

    print(tnt2.accion())
    print(tnt2.colocar("pared"))
    print(tnt2.romper())
    print()

    print(horno1.accion())
    print(horno1.colocar("suelo"))
    print(horno1.romper())
    print()

    print(horno2.accion())
    print(horno2.colocar("pared"))
    print(horno2.romper())


if __name__ == "__main__":
    main()