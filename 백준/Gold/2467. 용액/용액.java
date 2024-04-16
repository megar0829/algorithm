import java.awt.*;
import java.util.*;
import java.io.*;

public class Main {
    private static int N;
    private static int[] arr;
    public static void main(String[] args) throws IOException {
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(input.readLine());

        StringTokenizer st = new StringTokenizer(input.readLine());

        arr = new int[N];

        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        int ans = Integer.MAX_VALUE;

        int x = 0;
        int y = 0;

        int left = 0;
        int right = N - 1;

        while (true) {
            if (left >= right) {
                break;
            }

            if (ans == 0) {
                break;
            }

            int sumVal = arr[left] + arr[right];

            if (ans >= Math.abs(sumVal)) {
                ans = Math.abs(sumVal);
                x = arr[left];
                y = arr[right];
            }

            if (sumVal > 0) {
                right--;
            }
            else {
                left++;
            }
        }

        System.out.println(x + " " + y);
    }
}