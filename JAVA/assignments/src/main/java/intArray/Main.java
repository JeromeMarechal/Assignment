import java.util.ArrayList;
public class Main {
    public static void main(String[] args) {
        int n = 6;
        ArrayList<Integer> fibo = new ArrayList<>();

        fibo.add(0);
        fibo.add(1);

        for (int i = 2; i < n; i++) {
            fibo.add(fibo.get(i - 2) + fibo.get(i - 1));
        };

        System.out.println(fibo);

    }
}
