import java.util.PriorityQueue;
import java.util.Scanner;


public class Main {
    static int N;
    static PriorityQueue pQ = new PriorityQueue();

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        N = scanner.nextInt();

        for (int i = 0; i < N; i++) {
            int x = scanner.nextInt();

            if(x == 0){
                if(pQ.isEmpty())
                    System.out.println(0);
                else{
                    System.out.println(pQ.peek());
                    pQ.remove(pQ.peek());
                }
            }
            else{
                pQ.add(x);
            }
        }


    }
}
