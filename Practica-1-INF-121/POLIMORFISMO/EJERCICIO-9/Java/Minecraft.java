class BloqueCofre {
    private int capacidad;
    private int resistencia;
    private String tipo;

    public BloqueCofre(int capacidad, int resistencia, String tipo) {
        this.capacidad = capacidad;
        this.resistencia = resistencia;
        this.tipo = tipo;
    }

    public String accion() {
        return "Abriendo el cofre de tipo " + tipo + ".";
    }

    public String colocar(String orientacion) {
        return "Colocando el cofre en posición " + orientacion + ".";
    }

    public String romper() {
        return "Rompiendo el cofre de tipo " + tipo + ". Puede que se derramen los objetos dentro.";
    }
}

class BloqueTnt {
    private String tipo;
    private int daño;

    public BloqueTnt(String tipo, int daño) {
        this.tipo = tipo;
        this.daño = daño;
    }

    public String accion() {
        return "Activando el TNT de tipo " + tipo + ".";
    }

    public String colocar(String orientacion) {
        return "Colocando el TNT en posición " + orientacion + ".";
    }

    public String romper() {
        return "Rompiendo el TNT de tipo " + tipo + ". ¡Cuidado! Puede explotar.";
    }
}

class BloqueHorno {
    private String color;
    private int capacidadComida;

    public BloqueHorno(String color, int capacidadComida) {
        this.color = color;
        this.capacidadComida = capacidadComida;
    }

    public String accion() {
        return "Usando el horno de color " + color + ".";
    }

    public String colocar(String orientacion) {
        return "Colocando el horno en posición " + orientacion + ".";
    }

    public String romper() {
        return "Rompiendo el horno de color " + color + ". Puede que se rompa y se pierda comida.";
    }
}

public class Minecraft {
    public static void main(String[] args) {
        // Instanciar 2 bloques de cada tipo
        BloqueCofre cofre1 = new BloqueCofre(27, 5, "Madera");
        BloqueCofre cofre2 = new BloqueCofre(54, 10, "Metal");

        BloqueTnt tnt1 = new BloqueTnt("TNT Normal", 100);
        BloqueTnt tnt2 = new BloqueTnt("TNT Especial", 200);

        BloqueHorno horno1 = new BloqueHorno("Gris", 10);
        BloqueHorno horno2 = new BloqueHorno("Negro", 15);

        // Mostrar acciones y colocaciones
        System.out.println(cofre1.accion());
        System.out.println(cofre1.colocar("suelo"));
        System.out.println(cofre1.romper());
        System.out.println();

        System.out.println(cofre2.accion());
        System.out.println(cofre2.colocar("pared"));
        System.out.println(cofre2.romper());
        System.out.println();

        System.out.println(tnt1.accion());
        System.out.println(tnt1.colocar("suelo"));
        System.out.println(tnt1.romper());
        System.out.println();

        System.out.println(tnt2.accion());
        System.out.println(tnt2.colocar("pared"));
        System.out.println(tnt2.romper());
        System.out.println();

        System.out.println(horno1.accion());
        System.out.println(horno1.colocar("suelo"));
        System.out.println(horno1.romper());
        System.out.println();

        System.out.println(horno2.accion());
        System.out.println(horno2.colocar("pared"));
        System.out.println(horno2.romper());
    }
}