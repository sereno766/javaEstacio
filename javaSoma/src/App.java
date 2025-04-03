import java.util.Scanner;

public class App {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);


        System.out.println("digite um valor de inteiro");
        int valor = scanner.nextInt();
        
        System.out.println("digite um valor de inteiro");
        int valor2 = scanner.nextInt();
        
        int resultado = valor + valor2;
        System.out.println(resultado);
    
    }
}
