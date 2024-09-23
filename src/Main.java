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
        //question8();
        //question9();
        //question10();
        //question11();

//        Question1 q1 = new Question1();
//        q1.divMethod1();

//        Question2 q2 = new Question2();
//        q2.modMethod1();
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
        //Variable declaration and initialisation
        int preVatPrice = 5500;
        double vatRate = preVatPrice * 0.21; // VAT calculation

        //Price with VAT calculated
        double priceWithVat = preVatPrice + vatRate;

        System.out.println("Price before VAT: " + preVatPrice); //Print out Price Before VAT
        System.out.println("VAT at 21% is: " + vatRate); //VAT % calculated from given preVatPrice
        System.out.println("Price with VAT: " + priceWithVat); //Price with VAT printed from calculation in variable

    }
    static void question9() {
        int heightInInches = 73; //Declare and initialise variable heightInInches as int value

        int feet = heightInInches / 12; //Acquire height in feet by dividing inches height by 12
        int inches = heightInInches % 12; //Use mod to get the remaining inches

        System.out.println("Your height in feet and inches is: " + feet + "'" + inches + "\"");
        //Print statement with concatenated str and int values denoting height in feet and inches. Hopefully it works.
    }
    static void question10() {
        int partyGuests = 65; //declare variable and initialise for partyGuests
        int bottlesPerGuest = 1; //declare and initialise variable for bottlesPerGuest
        int bottlesPerBox = 25; //declare and initialise variable for bottlesPerBox
        System.out.println("You will require " + (partyGuests * bottlesPerGuest / bottlesPerBox) + " whole boxes and "
                + (partyGuests * bottlesPerGuest % bottlesPerBox) + " extra bottles.");
        //Print statement with str concatenated with expressions for whole boxes and extra bottles required.
        //Sub in 2 for bottlesPerGuest to answer question 10.1
    }
    static void question11() {
        int withdrawalAmount = 80;
        int fifties, twenties, tens, fives;

        fifties = withdrawalAmount / 50;
        withdrawalAmount = withdrawalAmount % 50;

        twenties = withdrawalAmount / 20;
        withdrawalAmount = withdrawalAmount % 20;

        tens = withdrawalAmount / 10;
        withdrawalAmount = withdrawalAmount % 10;

        fives = withdrawalAmount / 5;
        withdrawalAmount = withdrawalAmount % 5;

        System.out.println("You will receive: ");
        System.out.println(fifties + " €50 note(s)");
        System.out.println(twenties + " €20 note(s)");
        System.out.println(tens + " €10 note(s)");
        System.out.println(fives + " €5 note(s)");

    }
}
