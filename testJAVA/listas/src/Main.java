import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        List<String> mensagens = new ArrayList<>();
        mensagens.add("Mensagem 01");
        mensagens.add("Mensagem 02");
        mensagens.add("Mensagem 03");
        mensagens.add("Mensagem 04");

        System.out.printf("Quantidade de mensagens: %d%n", mensagens.size(),"\n");
    
        for (int i = 0; i <mensagens.size(); i++)
        {
            System.out.println(mensagens.get(i));
        }
    }

}