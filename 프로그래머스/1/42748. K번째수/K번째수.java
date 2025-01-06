import java.util.ArrayList;
import java.util.Arrays;
class Solution {
public static ArrayList<Integer> solution(int[] array, int[][] commands) {
        ArrayList<Integer> answer = new ArrayList<>();

        for (int[] command: commands) {
            command[0] = command[0] - 1;
            int size = command[1] - command[0];
            int[] slice = new int[size];

            for (int i = 0; i < slice.length; i++) {
                slice[i] = array[command[0]+i];
            }
            Arrays.sort(slice);
            answer.add(slice[command[2]-1]);
        }
        return answer;
    }
}