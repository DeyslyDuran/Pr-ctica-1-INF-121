//Un restaurante organiza a su personal mediante las siguientes clases: la clase Cocinero con nombre, sueldoMes,horasExtra, sueldoHora . La clase Mesero con nombre, sueldoMes,horasExtra y propina. La clase Administrativa con nombre, sueldo y cargo. 
//a) Instanciar 1 Cocinero, 2 objetos Mesero y 2 objetos Administrativo
//b) Sobrecargar el método SueldoTotal para mostrar el sueldo total, sumando las horas extra, considerando el sueldo por hora y la propina en caso de los meseros. 
//c) Sobrecargar el método para mostrar a aquellos Empleados que tengan SueldoMes igual a X.
class Empleado {
    protected String nombre;
    protected double sueldoMes;

    public Empleado(String nombre, double sueldoMes) {
        this.nombre = nombre;
        this.sueldoMes = sueldoMes;
    }

    public double getSueldoMes() {
        return sueldoMes;
    }

    public void mostrar() {
        System.out.println("Nombre: " + nombre);
        System.out.println("Sueldo Mensual: " + sueldoMes);
    }
}

class Cocinero extends Empleado {
    private double horasExtra;
    private double sueldoHora;

    public Cocinero(String nombre, double sueldoMes, double horasExtra, double sueldoHora) {
        super(nombre, sueldoMes);
        this.horasExtra = horasExtra;
        this.sueldoHora = sueldoHora;
    }

    // Sobrecarga del método SueldoTotal
    public double sueldoTotal() {
        return sueldoMes + (horasExtra * sueldoHora);
    }

    @Override
    public void mostrar() {
        super.mostrar();
        System.out.println("Sueldo Total: " + sueldoTotal());
    }
}

class Mesero extends Empleado {
    private double horasExtra;
    private double propina;

    public Mesero(String nombre, double sueldoMes, double horasExtra, double propina) {
        super(nombre, sueldoMes);
        this.horasExtra = horasExtra;
        this.propina = propina;
    }

    // Sobrecarga del método SueldoTotal
    public double sueldoTotal() {
        return sueldoMes + (horasExtra * 10) + propina; // Suponiendo que el sueldo por hora es 10
    }

    @Override
    public void mostrar() {
        super.mostrar();
        System.out.println("Sueldo Total: " + sueldoTotal());
    }
}

class Administrativo extends Empleado {
    private String cargo;

    public Administrativo(String nombre, double sueldoMes, String cargo) {
        super(nombre, sueldoMes);
        this.cargo = cargo;
    }

    @Override
    public void mostrar() {
        super.mostrar();
        System.out.println("Cargo: " + cargo);
    }
}

public class Restaurante {
    public static void main(String[] args) {
        // Instanciar 1 Cocinero, 2 Meseros y 2 Administrativos
        Cocinero cocinero = new Cocinero("Juan", 1500, 10, 15);
        Mesero mesero1 = new Mesero("Pedro", 1200, 5, 200);
        Mesero mesero2 = new Mesero("Maria", 1200, 3, 150);
        Administrativo admin1 = new Administrativo("Luis", 1800, "Gerente");
        Administrativo admin2 = new Administrativo("Ana", 1600, "Asistente");

        // Mostrar información de los empleados
        cocinero.mostrar();
        System.out.println();
        mesero1.mostrar();
        System.out.println();
        mesero2.mostrar();
        System.out.println();
        admin1.mostrar();
        System.out.println();
        admin2.mostrar();
        System.out.println();

        // Mostrar empleados con SueldoMes igual a 1200
        System.out.println("Empleados con SueldoMes igual a 1200:");
        mostrarEmpleadosConSueldo(1200, cocinero, mesero1, mesero2, admin1, admin2);
    }

    public static void mostrarEmpleadosConSueldo(double sueldoBuscado, Empleado... empleados) {
        for (Empleado empleado : empleados) {
            if (empleado.getSueldoMes() == sueldoBuscado) {
                empleado.mostrar();
                System.out.println();
            }
        }
    }
}