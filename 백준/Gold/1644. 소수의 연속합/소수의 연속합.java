import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Main {
    private static int N;

    public static void main(String[] args) throws IOException {
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(input.readLine());

        if (N == 1) {
            System.out.println(0);
        } else if (N < 4) {
            System.out.println(1);
        } else {
            boolean[] check = new boolean[N + 1];

            List<Integer> arr = new ArrayList<>();

            for (int i = 2; i < N + 1; i++) {
                if (!check[i]) {
                    arr.add(i);
                }

                for (int j = i * 2; j < N + 1; j += i) {
                    check[j] = true;
                }
            }

            int left = 0, right = 1;

            int sumVal = arr.get(left) + arr.get(right);

            int L = arr.size();

            int cnt = check[N] ? 0 : 1;

            while (true) {
                if (left >= right){
                    break;
                }

                if (sumVal == N) {
                    cnt++;

                    sumVal -= arr.get(left);

                    left++;
                } else if (sumVal < N) {
                    right++;

                    sumVal += arr.get(right);
                } else {
                    sumVal -= arr.get(left);

                    left++;
                }
            }

            System.out.println(cnt);
        }
    }
}