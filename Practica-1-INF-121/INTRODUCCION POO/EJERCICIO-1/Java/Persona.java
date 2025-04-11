public class Persona {

    public String nombre;
    public int edad ;
    public String ciudad;
    
    public Persona (String nombre, int edad, String ciudad){
        this.nombre=nombre;
        this.edad=edad;
        this.ciudad=ciudad;   
    }
    
    public void mostrarSaludo(){
        System.out.println("Hola, soy "+ nombre+ "de " + ciudad+".");
    }
    public boolean mayorDeEdad(){
        return edad >= 18;
    }
    public String getNombre(){
        return nombre;
    }
    public int getEdad(){
        return edad;
 
    }
    public String getCiudad(){
        return ciudad;
    }   
    
}
