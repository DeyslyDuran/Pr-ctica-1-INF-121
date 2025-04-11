#Realiza la abstracción de una Computadora
#a) Muestra los componentes principales de la computadora
#b) Muestra el estado de la computadora (encendido o apagado)
#c) Crea una instancia y simula encender y apagar la computadora.
class Computadora:
    def __init__(self):
        # Componentes principales de la computadora
        self.componentes = {
            "CPU": "Intel i7",
            "RAM": "16GB",
            "Almacenamiento": "1TB SSD",
            "Placa Base": "ASUS ROG",
            "Tarjeta Gráfica": "NVIDIA GTX 1660"
        }
        # Estado de la computadora
        self.estado = "apagada"

    def mostrar_componentes(self):
        print("Componentes de la computadora:")
        for componente, detalle in self.componentes.items():
            print(f"{componente}: {detalle}")

    def mostrar_estado(self):
        print(f"La computadora está {self.estado}.")

    def encender(self):
        if self.estado == "apagada":
            self.estado = "encendida"
            print("La computadora se ha encendido.")
        else:
            print("La computadora ya está encendida.")

    def apagar(self):
        if self.estado == "encendida":
            self.estado = "apagada"
            print("La computadora se ha apagado.")
        else:
            print("La computadora ya está apagada.")

# Crear una instancia de la computadora
mi_computadora = Computadora()

# Mostrar los componentes
mi_computadora.mostrar_componentes()

# Mostrar el estado inicial
mi_computadora.mostrar_estado()

# Encender la computadora
mi_computadora.encender()

# Mostrar el estado después de encender
mi_computadora.mostrar_estado()

# Apagar la computadora
mi_computadora.apagar()

# Mostrar el estado después de apagar
mi_computadora.mostrar_estado()