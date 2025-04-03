import java.time.LocalDate;
import java.time.Period;
import java.time.format.DateTimeFormatter;

public class App {
    public static void main(String[] args) {

        Pessoa pessoa1 = new Pessoa("Carlos", "10/05/1995", 175);
        pessoa1.exibirInfo();
    }
}

class Pessoa {
    private String nome;
    private String dataDeNascimento; 
    private int altura;

    public Pessoa(String nome, String dataDeNascimento, int altura) {
        this.nome = nome;
        this.dataDeNascimento = dataDeNascimento;
        this.altura = altura;
    }

    public int calcularIdade() {
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("dd/MM/yyyy");
        LocalDate dataNascimento = LocalDate.parse(this.dataDeNascimento, formatter);
        LocalDate dataAtual = LocalDate.now();

        return Period.between(dataNascimento, dataAtual).getYears();
    }

    public void exibirInfo() {
        System.out.println("Nome: " + nome);
        System.out.println("Data de Nascimento: " + dataDeNascimento);
        System.out.println("Altura: " + altura + " cm");
        System.out.println("Idade: " + calcularIdade() + " anos");
    }
}
