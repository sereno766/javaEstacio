import java.util.ArrayList;
import java.util.Scanner;

public class App {
    public static void main(String[] args)
    {
        ArrayList<Double>alunos = new ArrayList<>();
        for(int y =1; y<= 3; y++){

            Scanner scanner =new Scanner(System.in);
            ArrayList<Double>notas = new ArrayList<>();
            System.out.print("aluno"+y+":\n");
            for(int i=1; i<= 2;i++)
            {
                System.out.print("Digite sua nota"+i+":");
                double nota = scanner.nextDouble();
                notas.add(nota);
            
            }
            double soma =0;
            for(double nota : notas){
                soma += nota;
            }
            double media = soma / notas.size();
            alunos.add(media);
        }
        System.out.println("As médias dos alunos são:\n \n"
        + "Aluno 1: " + alunos.get(0) + " \n \n"
        + "Aluno 2: " + alunos.get(1) + " \n \n"
        + "Aluno 3: " + alunos.get(2));



    }
}
