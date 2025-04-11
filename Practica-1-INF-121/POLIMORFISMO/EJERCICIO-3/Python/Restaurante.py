class Empleado:
    def __init__(self, nombre, sueldo_mes):
        self.nombre = nombre
        self.sueldo_mes = sueldo_mes

    def mostrar(self):
        print(f"Nombre: {self.nombre}")
        print(f"Sueldo Mensual: {self.sueldo_mes}")

class Cocinero(Empleado):
    def __init__(self, nombre, sueldo_mes, horas_extra, sueldo_hora):
        super().__init__(nombre, sueldo_mes)
        self.horas_extra = horas_extra
        self.sueldo_hora = sueldo_hora

    def sueldo_total(self):
        return self.sueldo_mes + (self.horas_extra * self.sueldo_hora)

    def mostrar(self):
        super().mostrar()
        print(f"Sueldo Total: {self.sueldo_total()}")

class Mesero(Empleado):
    def __init__(self, nombre, sueldo_mes, horas_extra, propina):
        super().__init__(nombre, sueldo_mes)
        self.horas_extra = horas_extra
        self.propina = propina

    def sueldo_total(self):
        return self.sueldo_mes + (self.horas_extra * 10) + self.propina  # Suponiendo que el sueldo por hora es 10

    def mostrar(self):
        super().mostrar()
        print(f"Sueldo Total: {self.sueldo_total()}")

class Administrativo(Empleado):
    def __init__(self, nombre, sueldo_mes, cargo):
        super().__init__(nombre, sueldo_mes)
        self.cargo = cargo

    def mostrar(self):
        super().mostrar()
        print(f"Cargo: {self.cargo}")

def mostrar_empleados_con_sueldo(sueldo_buscado, *empleados):
    for empleado in empleados:
        if empleado.sueldo_mes == sueldo_buscado:
            empleado.mostrar()
            print()


cocinero = Cocinero("Juan", 1500, 10, 15)
mesero1 = Mesero("Pedro", 1200, 5, 200)
mesero2 = Mesero("Maria", 1200, 3, 150)
admin1 = Administrativo("Luis", 1800, "Gerente")
admin2 = Administrativo("Ana", 1600, "Asistente")


cocinero.mostrar()
print()
mesero1.mostrar()
print()
mesero2.mostrar()
print()
admin1.mostrar()
print()
admin2.mostrar()
print()


print("Empleados con SueldoMes igual a 1200:")
mostrar_empleados_con_sueldo(1200, cocinero, mesero1, mesero2, admin1, admin2)