import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Integer N = Integer.parseInt(br.readLine());

        PriorityQueue<Integer> card = new PriorityQueue<>();

        for (int i = 0; i < N; i++) {
            card.add(Integer.parseInt(br.readLine()));
        }
        
        int num = 0;
        while (card.size() > 1){
            int d1 = card.poll();
            int d2 = card.poll();
            
            num += d1 + d2;
            card.add(d1+d2);
        }
        System.out.println(num);
    }
}