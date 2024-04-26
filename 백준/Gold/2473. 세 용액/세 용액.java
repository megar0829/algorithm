import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    private static int N;
    private static long[] arr;

    public static void main(String[] args) throws IOException {
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(input.readLine());

        StringTokenizer st = new StringTokenizer(input.readLine());

        arr = new long[N];

        for (int i = 0; i < N; i++) {
            arr[i] = Long.parseLong(st.nextToken());
        }

        Arrays.sort(arr);

        long MAX_LONG = Long.MAX_VALUE;

        long[] ans = new long[3];

        for (int i = 0; i < N - 2; i++) {
            int left = i + 1;
            int right = N - 1;

            while (left < right) {
                long sumVal = arr[i] + arr[left] + arr[right];

                if (Math.abs(sumVal) < MAX_LONG) {
                    MAX_LONG = Math.abs(sumVal);
                    ans = new long[]{arr[i], arr[left], arr[right]};
                }

                if (sumVal < 0) {
                    left++;
                } else if (sumVal > 0) {
                    right--;
                } else {
                    break;
                }
            }
        }

        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < 3; i++) {
            sb.append(ans[i]).append(" ");
        }

        System.out.println(sb);
    }
}