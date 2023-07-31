import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static Boolean[][] visited;
    static int[][] map;
    static int N, count;

    static int[] dx = new int[]{-1, 1, 0, 0};
    static int[] dy = new int[]{0, 0, -1, 1};
    static List<Integer> result = new ArrayList<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());

        map = new int[N][N];
        visited = new Boolean[N][N];

        for (int i = 0; i < N; i++) {
            String[] temp = br.readLine().split("");
            for (int j = 0; j < N; j++) {
                map[i][j] = Integer.parseInt(temp[j]);
                visited[i][j] = Boolean.FALSE;
            }
        }

        
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                count = 0;

                // 해당 위치에 건물이 있고, 방문하지 않았으면 DFS 탐색
                if (map[i][j]==1 && !visited[i][j]){
                    DFS(i,j);
                    count++;
                    result.add(count);
                }
            }
        }
        
        
        // 총 단지 수
        System.out.println(result.size());
        
        // 각 단지내 집의 수 + 오름차순 정렬
        Collections.sort(result);
        Iterator i = result.iterator();
        while(i.hasNext())
            System.out.println(i.next());

    }

    static void DFS(int x, int y){
        visited[x][y] = Boolean.TRUE;

        // x, y로 양방향 탐색
        for (int i = 0; i < 4; i++) {
            // 상하좌우로 다른 집이 있는지 찾기 위해 dx, dy를 사용
            int new_x = x + dx[i];
            int new_y = y + dy[i];

            // 0과 N은 탐색 범위를 벗어나지 않게 제한을 두는 것
            //범위에 벗어나지 않고 탐색 조건에 맞으면 DFS 탐색
            if (new_x>=0 && new_y>=0 && new_x<N && new_y<N && !visited[new_x][new_y] && map[new_x][new_y]==1){
                DFS(new_x, new_y);
                count++;
            }
        }
    }
}
