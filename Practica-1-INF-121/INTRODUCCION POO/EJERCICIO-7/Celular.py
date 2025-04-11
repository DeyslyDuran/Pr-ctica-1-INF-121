#Crea una clase Celular con espacio para 20 aplicaciones o 1024Mb de Espacio
#a) Crea un método para instalar una nueva aplicación
#b) Crea un método para utilizar una aplicación (las aplicaciones que pesan más
#de 100Mb utilizan un 2% de batería por cada 10 minutos uso, las que pesan
#más de 250Mb utilizan 5% por cada 10 minutos de uso, en otros casos utiliza
#un 1% cada 10 minutos de uso)
#c) Muestra el porcentaje de batería restante
#d) Cuando la batería se acabe al tratar de utilizar el celular este debe mostrar el
#mensaje de celular apagado
class Aplicacion:
    def __init__(self, nombre, tamaño):
        self.nombre = nombre
        self.tamaño = tamaño  # Tamaño en MB

class Celular:
    def __init__(self):
        self.aplicaciones = []  # Lista paralmacenar aplicaciones
        self.espacio_total = 1024  # Espacio total en MB
        self.espacio_usado = 0  # Espacio usado en MB
        self.bateria = 100  # Porcentaje de batería

    def instalar_aplicacion(self, app):
        if len(self.aplicaciones) < 20 and (self.espacio_usado + app.tamaño) <= self.espacio_total:
            self.aplicaciones.append(app)
            self.espacio_usado += app.tamaño
            print(f"Aplicación '{app.nombre}' instalada.")
        else:
            print("No se puede instalar la aplicación. Espacio insuficiente o límite de aplicaciones alcanzado.")

    def utilizar_aplicacion(self, nombre_app, minutos):
        if self.bateria <= 0:
            print("Celular apagado.")
            return

        for app in self.aplicaciones:
            if app.nombre == nombre_app:
                if app.tamaño > 250:
                    consumo = 5 * (minutos // 10)  # 5% cada 10 minutos
                elif app.tamaño > 100:
                    consumo = 2 * (minutos // 10)  # 2% cada 10 minutos
                else:
                    consumo = 1 * (minutos // 10)  # 1% cada 10 minutos

                self.bateria -= consumo
                if self.bateria < 0:
                    self.bateria = 0  # No permitir que la batería sea negativa
                print(f"Usando '{app.nombre}' por {minutos} minutos. Batería restante: {self.bateria}%")
                return

        print(f"La aplicación '{nombre_app}' no está instalada.")

    def mostrar_bateria(self):
        print(f"Batería restante: {self.bateria}%")


# Ejemplo de uso
celular = Celular()

# Crear aplicaciones
app1 = Aplicacion("WhatsApp", 50)
app2 = Aplicacion("Facebook", 150)
app3 = Aplicacion("Juego Pesado", 300)

# Instalar aplicaciones
celular.instalar_aplicacion(app1)
celular.instalar_aplicacion(app2)
celular.instalar_aplicacion(app3)

# Utilizar aplicaciones
celular.utilizar_aplicacion("WhatsApp", 30)  # 3% de batería
celular.utilizar_aplicacion("Facebook", 20)  # 8% de batería
celular.utilizar_aplicacion("Juego Pesado", 15)  # 25% de batería

# Mostrar batería restante
celular.mostrar_bateria()

# Intentar usar el celular cuando la batería se ha agotado
celular.bateria = 0  # Simular batería agotada
celular.utilizar_aplicacion("WhatsApp", 10)  # Debería mostrar "Celular apagado."