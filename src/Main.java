//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    public static void main(String[] args) {
        //divMethod();
        //modMethod();
        //whatEver1();
        //Whatever();
        //question6();
        //question7();
        question8();
    }
    static void divMethod() {
        System.out.println("Answer 1 is " + (9/4));
        System.out.println("Answer 2 is " + (17/3));
    }
    static void modMethod() {
        System.out.println("Answer 1 is " + (9%4));
        System.out.println("Answer 2 is " + (17%3));
    }
    static void whatEver1() {
        System.out.println("Java programming");
    }
    static void Whatever() {
        int randomNumber1 = (int)(Math.random() * 47) + 1;
        int randomNumber2 = (int)(Math.random() * 47) + 1;

        System.out.println("Output 1 is " + randomNumber1);
        System.out.println("Output 2 is " + randomNumber2);
    }
    static void question6() {
        int randomNumber1 = (int)(Math.random() * 51) + 50;
        int randomNumber2 = (int)(Math.random() * 51) + 50;

        System.out.println("Output 1 is " + randomNumber1);
        System.out.println("Output 2 is " + randomNumber2);
    }
    static void question7() {
        int aNumber = (int)(Math.random() * 90) + 10;
        String numStr = Integer.toString(aNumber);
                char leftDgt = numStr.charAt(0);
                char rightDgt = numStr.charAt(1);
        System.out.println(leftDgt + ":" + rightDgt);
    }
    static void question8() {
        int preVatPrice = 5500; //Used int to store whole number
        double VAT_RATE = 0.21; //Used double to store decimal value
        double VAT = preVatPrice * VAT_RATE; //Used double for decimal value, calculating VAT amount due
        double withVat = preVatPrice + VAT;

        System.out.println("Pre VAT Price: 5500");
        System.out.printf();
    }
}