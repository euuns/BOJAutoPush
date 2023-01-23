import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int num1 = scanner.nextInt();
        int num2 = scanner.nextInt();

        int one = num2%10;
        int ten = num2%100/10;
        int hun = num2/100;

        System.out.println(num1*one);
        System.out.println(num1*ten);
        System.out.println(num1*hun);
        System.out.println(num1*num2);
    }
}