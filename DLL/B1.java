import java.util.Scanner;

public class B1 {

    static{
        System.loadLibrary("B1");
    }

    private native int add(int a, int b);
    private native int sub(int a, int b);
    private native int mul(int a, int b);
    private native int div(int a, int b);


    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        int a,b,choice;

        System.out.println("Enter first number: ");
        a = scanner.nextInt();

        System.out.println("Enter second number: ");
        b = scanner.nextInt();

        
        B1 calculator = new B1();

        
        System.out.println("\nEnter your choice:");
        choice = scanner.nextInt();

        switch (choice) {
            case 1:
                calculator.add(a, b);
                break;
            case 2:
                calculator.sub(a, b);
                break;
            case 3:
                calculator.mul(a, b);
                break;
            case 4:
                calculator.div(a, b);
                break;
            default:
                System.out.println("Invalid choice.");
                break;
        }
        
        scanner.close();
    }
}
