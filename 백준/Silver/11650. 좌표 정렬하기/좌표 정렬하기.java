import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int num = Integer.parseInt(scanner.nextLine());

        List<int[]> list = new ArrayList<>();

        for (int i = 0; i < num; i++) {
            String[] input = scanner.nextLine().split(" ");
            int[] coordinate = new int[]{Integer.parseInt(input[0]), Integer.parseInt(input[1])};
            list.add(coordinate);
        }

        Collections.sort(list, (o1, o2) -> o1[0] == o2[0] ? o1[1] - o2[1] : o1[0] - o2[0]);
        for (int[] sort:list) {
            System.out.println(sort[0] + " " + sort[1]);
        }
    }
}