#Crea una clase Persona con nombre, edad y ciudad
class Persona:
    def __init__ (self , nombre,edad,ciudad):
        self.nombre=nombre
        self.edad = edad
        self.ciudad = ciudad
    #a) Agrega un método para mostrar el saludo: “Hola, soy {nombre} de {ciudad}”
    def mostrarSaludo (self):
        print(f"Hola , soy {self.nombre} de {self.ciudad}.")
    #c) Agrega un método para verificar si es mayor de edad
    def es_mayor (self):
        return self.edad >= 18
#b) Crea tres personas y muestra su saludo
persona1 = Persona("Deysly", 18, "La Paz")
persona2 = Persona("Angel", 23, "Cochabamba")
persona3 = Persona("Ledys", 30, "Riberalta")

# Mostrar saludos
persona1.mostrarSaludo()
persona2.mostrarSaludo()
persona3.mostrarSaludo()

# Verificar si son mayores de edad
print(f"{persona1.nombre} es mayor de edad: {persona1.es_mayor()}")
print(f"{persona2.nombre} es mayor de edad: {persona2.es_mayor()}")
print(f"{persona3.nombre} es mayor de edad: {persona3.es_mayor()}") 
    
