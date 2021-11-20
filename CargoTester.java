public class CargoTester 
{
    public static void main(String[] args) 
    {
        testSuite();
    }

    static void testSuite()
    {
        test12();
        test22();
        test23();
        test26();
        test27();
        test43();
    }

    static void test12()
    {
        try {
            Demo.opg1();
            System.out.println("1.2: \t\t\tPass");
        } catch (Exception e) {
            System.out.println("1.2: \t\t\tError");
        }
    }

    static void test22()
    {
        try {
            new Booking("bookingId", 0, false, new Container(0, 0));
            System.out.println("2.2: \t\t\tError");
        } catch (InvalidKgException e) {
            System.out.println("2.2: \t\t\tPass");
        }
    }

    static void test23()
    {
        try {
            CargoShip cs = new CargoShip("t",1,1);
            cs.addBooking("jaaj", 0, true, 0, 0);
            System.out.println("2.3: \t\t\tPass");
            if (false) throw new InvalidKgException();
        } catch (InvalidKgException e) {
            System.out.println("2.3: \t\t\tError");
        }
    }

    static void test26()
    {
        try {
            CargoShip cs = new CargoShip("t",1,1);
            cs.addBooking("jaaj", 1, true, 0, 0);
            cs.checkAddBooking("jaaj", 1, true, 0, 0);
            System.out.println("2.6: \t\t\tError");
        } catch (ContainerAlreadyBookedException e) {
            System.out.println("2.6: \t\t\tPass");
        }
    }

    static void test27()
    {
        try {
            Demo.opg2();
            System.out.println("2.7: \t\t\tPass");
        } catch (Exception e) {
            System.out.println("2.7: \t\t\tError");
        }
    }

    static void test43()
    {
        Demo.opg4();
    }
}