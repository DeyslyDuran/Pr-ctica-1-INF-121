//Sea la clase Videojuego:

//a) Instanciar al menos 2 videojuegos
//b) Sobrecargar el constructor 2 veces
//c) Implementar un método mostrar()
//d) Sobrecargar el método agregarJugadores() donde en el primero se agregue
//solo 1 jugador y en otro se ingrese una cantidad de jugadores a aumentar.
class Videojuego {
    private String nombre;
    private String plataforma;
    private int cantidadJugadores;

    
    public Videojuego() {
        this.nombre = "Desconocido";
        this.plataforma = "Desconocida";
        this.cantidadJugadores = 0;
    }

    
    public Videojuego(String nombre, String plataforma) {
        this.nombre = nombre;
        this.plataforma = plataforma;
        this.cantidadJugadores = 0;
    }

    
    public Videojuego(String nombre, String plataforma, int cantidadJugadores) {
        this.nombre = nombre;
        this.plataforma = plataforma;
        this.cantidadJugadores = cantidadJugadores;
    }

    
    public void mostrar() {
        System.out.println("Nombre: " + nombre);
        System.out.println("Plataforma: " + plataforma);
        System.out.println("Cantidad de Jugadores: " + cantidadJugadores);
    }

    
    public void agregarJugadores() {
        this.cantidadJugadores++;
    }

    
    public void agregarJugadores(int cantidad) {
        if (cantidad > 0) {
            this.cantidadJugadores += cantidad;
        } else {
            System.out.println("La cantidad de jugadores a agregar debe ser mayor que 0.");
        }
    }

    public static void main(String[] args) {
        
        Videojuego juego1 = new Videojuego("The Legend of Zelda", "Nintendo Switch");
        Videojuego juego2 = new Videojuego("Call of Duty", "PC", 4);

        
        juego1.mostrar();
        System.out.println();
        juego2.mostrar();
        System.out.println();

        
        juego1.agregarJugadores();
        juego1.agregarJugadores(3);

        
        System.out.println("Después de agregar jugadores:");
        juego1.mostrar();
    }
}