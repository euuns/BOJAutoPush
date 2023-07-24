import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Integer N = Integer.parseInt(br.readLine());
        StringTokenizer st;

        List<Integer> stack = new ArrayList<>();

        for (int i = 0; i < N; i++) {

            st = new StringTokenizer(br.readLine());
            String opr = st.nextToken();

            if(opr.equals("push")) {
                Integer num = Integer.parseInt(st.nextToken());
                stack.add(num);
            }

            else if (opr.equals("pop")) {
                if(stack.isEmpty())
                    System.out.println(-1);
                else 
                    System.out.println(stack.remove(stack.size() - 1));
            }

            else if (opr.equals("top"))
                if(stack.isEmpty())
                    System.out.println(-1);
                else
                    System.out.println(stack.get(stack.size()-1));

            else if (opr.equals("size"))
                System.out.println(stack.size());

            else if (opr.equals("empty")){
                if (stack.isEmpty())
                    System.out.println(1);
                else
                    System.out.println(0);
            }
        }
    }
}