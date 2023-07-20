import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

// BOJ 11724
public class Main {

    static ArrayList<Integer>[] A;
    static boolean visited[];

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        // n:노드, m:간선
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        // n개의 노드를 가진 ArrayList생성
        // 1번 인덱스부터 시작하여 노드 사용 -> 배열 크기는 n+1
        A = new ArrayList[n+1];
        visited = new boolean[n+1];

        for (int i = 0; i < n+1; i++) {
            A[i] = new ArrayList<Integer>();
        }

        // 간선 수만큼 반복하여 노드를 연결
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());

            int s = Integer.parseInt(st.nextToken());   //노드
            int e = Integer.parseInt(st.nextToken());   //간선

            // 해당 노드에 연결
            // 방향이 없는 그래프로 양쪽 노드를 모두 같이 연결
            A[s].add(e);
            A[e].add(s);
        }

        int count = 0;
        for (int i = 0; i < n+1; i++) {
            // 모든 노드를 방문할 때까지 반복하여 그래프가 몇개 나오는지 count를 증가시킨다.
            if(!visited[i]) {
                count++;
                DFS(i);
            }
        }

        System.out.println(count-1);
    }

    static void DFS(int v){
        // 모든 그래프를 방문했으면 return
        if(visited[v]){ return; }

        // v 정점을 방문하면 true로 변경
        visited[v] = true;
        // 그래프와 연결된 노드를 모두 확인
        for(int i: A[v]){
            // 만약 연결된 노드 중 방문하지 않은 노드가 있으면 방문
            if(visited[i] == false){ DFS(i); }
        }
    }
}
