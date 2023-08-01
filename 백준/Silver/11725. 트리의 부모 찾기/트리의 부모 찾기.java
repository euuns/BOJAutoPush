import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
    static int N;
    static ArrayList<ArrayList<Integer>> tree = new ArrayList<>();
    static Boolean[] visited;

    static int[] result;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        N = Integer.parseInt(br.readLine());

        visited = new Boolean[N+1];
        result = new int[N+1];

        for (int i = 0; i < N+1; i++) {
            tree.add(new ArrayList<>());
            visited[i] = Boolean.FALSE;
        }

        for (int i = 0; i < N-1; i++) {
            st = new StringTokenizer(br.readLine());
            Integer node = Integer.parseInt(st.nextToken());
            Integer edgeNode = Integer.parseInt(st.nextToken());

            tree.get(edgeNode).add(node);
            tree.get(node).add(edgeNode);
        }

        DFS(1);

        // 2번 노드부터 순서대로 출력
        for (int i = 2; i < N+1; i++) {
            System.out.println(result[i]);
        }
    }

    public static void DFS(int start){
        visited[start] = Boolean.TRUE;

        // start와 연결된 노드 i를 구할 수 있음
        for (Integer i:tree.get(start)) {
            if(!visited[i]){
                // i의 부모는 start, 결과 배열에 i노드의 부모 start를 저장
                result[i] = start;
                DFS(i);
            }
        }
    }
}