#Crea una clase Estudiante con nombre, nota_1, nota_2
class Estudiante:
    def __init__(self, nombre, nota_1, nota_2):
        self.nombre = nombre
        self.nota_1 = nota_1
        self.nota_2 = nota_2
#a) Agrega un método para calcular el promedio
    def calcular_promedio(self):
        return (self.nota_1 + self.nota_2) / 2
#b) Agrega un método para verificar si aprobó (promedio >=6)
    def verificar_aprobacion(self):
        promedio = self.calcular_promedio()
        return promedio >= 6


#c) Crea tres estudiantes, muestra sus promedios y si aprobaron
estudiante1 = Estudiante("Alice", 7.5, 8.0)
estudiante2 = Estudiante("Angel", 5.0, 6.0)
estudiante3 = Estudiante("Deysly", 9.0, 10.0)


for estudiante in [estudiante1, estudiante2, estudiante3]:
    promedio = estudiante.calcular_promedio()
    aprobado = estudiante.verificar_aprobacion()
    estado = "aprobó" if aprobado else "no aprobó"
    print(f"{estudiante.nombre} tiene un promedio de {promedio:.2f} y {estado}.") 