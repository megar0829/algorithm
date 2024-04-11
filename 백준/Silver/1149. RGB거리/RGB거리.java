import java.awt.*;
import java.util.*;
import java.io.*;

public class Main {
    private static int N;
    private static int[][] arr;
    private static int[][] dp;

    private static int ans;

    public static void main(String[] args) throws IOException {
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(input.readLine());

        arr = new int[N][3];

        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(input.readLine());
            int r, g, b;

            r = Integer.parseInt(st.nextToken());
            g = Integer.parseInt(st.nextToken());
            b = Integer.parseInt(st.nextToken());

            arr[i][0] = r;
            arr[i][1] = g;
            arr[i][2] = b;
        }

        dp = new int[N][3];

        ans = 100000000;

        dp[0][0] = arr[0][0];
        dp[0][1] = arr[0][1];
        dp[0][2] = arr[0][2];

        for (int i = 1; i < N; i++) {
            dp[i][0] = Math.min(dp[i - 1][1] + arr[i][0], dp[i - 1][2] + arr[i][0]);
            dp[i][1] = Math.min(dp[i - 1][0] + arr[i][1], dp[i - 1][2] + arr[i][1]);
            dp[i][2] = Math.min(dp[i - 1][0] + arr[i][2], dp[i - 1][1] + arr[i][2]);
        }

        for (int i = 0; i < 3; i++) {
            ans = Math.min(ans, dp[N - 1][i]);
        }

        System.out.println(ans);
    }
}