import java.util.Scanner;

public class Calculator {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double num1, num2;
        char operator;
        boolean end = false;

        while (!end) {
            System.out.print("请输入第1个数字: ");
            num1 = scanner.nextDouble();

            System.out.print("请输入运算符 (+, -, *, /) 或按 'q' 退出: ");
            operator = scanner.next().charAt(0);

            if (operator == 'q') {
                end = true;
                continue;
            }

            System.out.print("请输入第2个数字: ");
            num2 = scanner.nextDouble();

            switch (operator) {
                case '+':
                    System.out.println("结果: " + (num1 + num2));
                    break;
                case '-':
                    System.out.println("结果: " + (num1 - num2));
                    break;
                case '*':
                    System.out.println("结果: " + (num1 * num2));
                    break;
                case '/':
                    if (num2 == 0) {
                        System.out.println("除数不能为0！");
                    } else {
                        System.out.println("结果: " + (num1 / num2));
                    }
                    break;
                default:
                    System.out.println("无效的运算符！");
                    break;
            }
        }

        scanner.close();
    }
}