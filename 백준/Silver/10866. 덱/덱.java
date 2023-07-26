import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        Deque<Integer> dQ = new ArrayDeque<>();

        Integer N = Integer.parseInt(br.readLine());

        for (int i = 0; i < N; i++) {

            st = new StringTokenizer(br.readLine()," ");
            String op = st.nextToken();

            if (op.equals("push_front")){
                dQ.offerFirst(Integer.parseInt(st.nextToken()));
            } else if (op.equals("push_back")) {
                dQ.offerLast(Integer.parseInt(st.nextToken()));
            }

            else if (op.equals("pop_front")){
                if (dQ.isEmpty())
                    System.out.println(-1);
                else
                    System.out.println(dQ.pollFirst());
            } else if (op.equals("pop_back")){
                if (dQ.isEmpty())
                    System.out.println(-1);
                else
                    System.out.println(dQ.pollLast());
            }

            else if (op.equals("size"))
                System.out.println(dQ.size());

            else if (op.equals("empty")){
                if (dQ.isEmpty())
                    System.out.println(1);
                else System.out.println(0);
            }

            else if (op.equals("front")){
                if (dQ.isEmpty())
                    System.out.println(-1);
                else
                    System.out.println(dQ.peekFirst());
            } else if (op.equals("back")) {
                if (dQ.isEmpty())
                    System.out.println(-1);
                else
                    System.out.println(dQ.peekLast());
            }
        }
    }
}
