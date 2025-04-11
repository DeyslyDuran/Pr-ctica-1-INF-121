//Crea una clase Coche con marca, modelo y velocidad
class Coche {
    public  String marca;
    public String modelo;
    public  int velocidad; 

    
    public Coche(String marca, String modelo) {
        this.marca = marca;
        this.modelo = modelo;
        this.velocidad = 0; 
    }

    //a) Agrega un método acelerar () que aumente la velocidad en 10
    public void acelerar() {
        velocidad += 10;
        System.out.println(marca + " " + modelo + " ha acelerado. Velocidad actual: " + velocidad + " km/h");
    }

    //b) Agrega un método frenar () que disminuya la velocidad en 5
    public void frenar() {
        velocidad -= 5;
        if (velocidad < 0) {
            velocidad = 0; 
        }
        System.out.println(marca + " " + modelo + " ha frenado. Velocidad actual: " + velocidad + " km/h");
    }

    
    public int getVelocidad() {
        return velocidad;
    }
}
//c) Crea dos coches, aceléralos, frénalos y muestra sus velocidades
public class Aplicacion {
    public static void main(String[] args) {
        
        Coche coche1 = new Coche("Toyota", "Corolla");
        Coche coche2 = new Coche("Ford", "Focus");

        
        coche1.acelerar();
        coche2.acelerar();

        
        coche1.frenar();
        coche2.frenar();

        
        System.out.println("Velocidad final de " + coche1.marca + " " + coche1.modelo + ": " + coche1.getVelocidad() + " km/h");
        System.out.println("Velocidad final de " + coche2.marca + " " + coche2.modelo + ": " + coche2.getVelocidad() + " km/h");
    }
}
