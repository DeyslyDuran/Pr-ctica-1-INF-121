public class Main{
    public static void main (String [] args){
        Persona persona1= new Persona ("Deysly" , 19 , "La Paz");
        Persona persona2=new Persona("Angel",23,"Cochabamba");
        Persona persona3 = new Persona("Ledys",12,"Riberalta");
        
        persona1.mostrarSaludo();
        persona2.mostrarSaludo();
        persona3.mostrarSaludo();
        
        System.out.println(persona1.getNombre()+" es mayor de edad");
        System.out.println(persona2.getNombre()+" es mayor de edad");
        System.out.println(persona3.getNombre()+" es mayor de edad");
    }
    
}