import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        Stack<Integer> stack = new Stack<>();

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        Integer N = Integer.parseInt(br.readLine());

        for (int i = 0; i < N; i++) {

            st = new StringTokenizer(br.readLine());
            String opr = st.nextToken();

            if(opr.equals("push")) {
                Integer num = Integer.parseInt(st.nextToken());
                stack.push(num);
            }

            else if (opr.equals("pop")) {
                if(stack.empty())
                    System.out.println(-1);
                else
                    System.out.println(stack.pop());
            }

            else if (opr.equals("top"))
                if(stack.empty())
                    System.out.println(-1);
                else
                    System.out.println(stack.peek());

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
