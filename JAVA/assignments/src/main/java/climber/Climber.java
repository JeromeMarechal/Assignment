package climber;

public class Climber {
    public static int climb(int n) {
        if (n < 0) {
            throw new IllegalArgumentException("Error: n connot be negative.");
        }

        int start = 0;
        int suite = 1;

        for (int i = 0; i < n; i++) {
            int temp = suite;
            suite = start + suite;
            start = temp;
        }

        return suite;

    }
}
