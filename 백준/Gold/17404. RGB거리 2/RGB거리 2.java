import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    private static int N;
    private static int[][] arr;
    private static int R, G, B;

    private static int[][] dp;
    private static int[] paint;

    public static void main(String[] args) throws IOException {
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(input.readLine());

        arr = new int[N + 1][3];

        for (int i = 1; i < N + 1; i++) {
            StringTokenizer st = new StringTokenizer(input.readLine());

            R = Integer.parseInt(st.nextToken());
            G = Integer.parseInt(st.nextToken());
            B = Integer.parseInt(st.nextToken());

            arr[i][0] = R;
            arr[i][1] = G;
            arr[i][2] = B;
        }

        dp = new int[N + 1][3];

        paint = new int[3];

        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                if (i == j) {
                    dp[1][j] = arr[1][j];
                } else {
                    dp[1][j] = 1001;
                }
            }

            for (int k = 2; k < N + 1; k++) {
                dp[k][0] = Math.min(dp[k - 1][1], dp[k - 1][2]) + arr[k][0];
                dp[k][1] = Math.min(dp[k - 1][2], dp[k - 1][0]) + arr[k][1];
                dp[k][2] = Math.min(dp[k - 1][0], dp[k - 1][1]) + arr[k][2];

                if (k == N) {
                    if (i == 0) {
                        paint[i] = Math.min(dp[N][1], dp[N][2]);
                    }
                    if (i == 1) {
                        paint[i] = Math.min(dp[N][2], dp[N][0]);
                    }
                    if (i == 2) {
                        paint[i] = Math.min(dp[N][0], dp[N][1]);
                    }
                }
            }
        }

        System.out.println(Math.min(paint[0], Math.min(paint[1], paint[2])));
    }
}