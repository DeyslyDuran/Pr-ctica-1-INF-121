#
#
#
#
class Oficina:
    def __init__(self, nro_sillas, nro_escritorios, nro_estanterias):
        self.nro_sillas = nro_sillas
        self.nro_escritorios = nro_escritorios
        self.nro_estanterias = nro_estanterias

    def mostrar(self):
        print("Oficina:")
        print(f"Número de Sillas: {self.nro_sillas}")
        print(f"Número de Escritorios: {self.nro_escritorios}")
        print(f"Número de Estanterías: {self.nro_estanterias}")

    def cantidad_muebles(self):
        return self.nro_sillas + self.nro_escritorios + self.nro_estanterias


class Aula:
    def __init__(self, nombre, capacidad, nro_pupitres):
        self.nombre = nombre
        self.capacidad = capacidad
        self.nro_pupitres = nro_pupitres

    def mostrar(self):
        print("Aula:")
        print(f"Nombre: {self.nombre}")
        print(f"Capacidad: {self.capacidad}")
        print(f"Número de Pupitres: {self.nro_pupitres}")

    def cantidad_muebles(self):
        return self.nro_pupitres


class Laboratorio:
    def __init__(self, nombre, capacidad, nro_mesas, nro_sillas):
        self.nombre = nombre
        self.capacidad = capacidad
        self.nro_mesas = nro_mesas
        self.nro_sillas = nro_sillas

    def mostrar(self):
        print("Laboratorio:")
        print(f"Nombre: {self.nombre}")
        print(f"Capacidad: {self.capacidad}")
        print(f"Número de Mesas: {self.nro_mesas}")
        print(f"Número de Sillas: {self.nro_sillas}")

    def cantidad_muebles(self):
        return self.nro_mesas + self.nro_sillas


def Universidad():
    
    oficina1 = Oficina(5, 3, 2)
    oficina2 = Oficina(4, 2, 1)

    aula1 = Aula("Aula 101", 30, 15)
    aula2 = Aula("Aula 102", 25, 12)

    laboratorio = Laboratorio("Laboratorio de Química", 20, 10, 5)

    
    oficina1.mostrar()
    print(f"Cantidad de Muebles: {oficina1.cantidad_muebles()}\n")

    oficina2.mostrar()
    print(f"Cantidad de Muebles: {oficina2.cantidad_muebles()}\n")

    aula1.mostrar()
    print(f"Cantidad de Muebles: {aula1.cantidad_muebles()}\n")

    aula2.mostrar()
    print(f"Cantidad de Muebles: {aula2.cantidad_muebles()}\n")

    laboratorio.mostrar()
    print(f"Cantidad de Muebles: {laboratorio.cantidad_muebles()}\n")


if __name__ == "__main__":
    Universidad()