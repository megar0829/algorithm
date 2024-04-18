import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    
    private static int N;
    private static int[] arr;
    private static int M;
    
    private static int[][] dp;
    public static void main(String[] args) throws IOException {
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(input.readLine());

        StringTokenizer st = new StringTokenizer(input.readLine());

        arr = new int[N + 1];

        for (int i = 1; i < N + 1; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        dp = new int[N + 1][N + 1];

        for (int i = 1; i < N + 1; i++) {
            dp[i][i] = 1;
        }

        for (int i = 1; i < N; i++) {
            if (arr[i] == arr[i + 1]) {
                dp[i][i + 1] = 1;
            }
        }

        for (int i = 2; i < N; i++) {
            for (int j = 1; j <= N - i; j++) {
                if ((arr[j] == arr[j + i]) && dp[j + 1][j + i - 1] == 1) {
                    dp[j][j + i] = 1;
                }
            }
        }

        M = Integer.parseInt(input.readLine());

        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(input.readLine());

            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            sb.append(dp[a][b]);

            if (i != M - 1) {
                sb.append("\n");
            }
        }

        System.out.print(sb);
    }
}