import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        LinkedList<Integer> list = new LinkedList<>();

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        Integer N = Integer.parseInt(br.readLine());
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            String oper = st.nextToken();

            if(oper.equals("push")){
                Integer num = Integer.parseInt(st.nextToken());
                list.add(num);
            }

            else if (oper.equals("pop")){
                if (list.isEmpty()) System.out.println(-1);
                else
                    System.out.println(list.pollFirst());
            }

            else if (oper.equals("size"))
                System.out.println(list.size());

            else if (oper.equals("empty")){
                if (list.isEmpty())
                    System.out.println(1);
                else System.out.println(0);
            }

            else if (oper.equals("front")){
                if (list.isEmpty())
                    System.out.println(-1);
                else System.out.println(list.getFirst());
            }

            else if (oper.equals("back")){
                if (list.isEmpty())
                    System.out.println(-1);
                else System.out.println(list.getLast());
            }
        }
    }
}
