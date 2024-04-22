import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    private static int T;
    private static int N, K;
    private static int[] delays;
    private static List<List<Integer>> arr;
    private static int X, Y;
    private static int W;
    private static int[] count;
    private static int[] dp;
    private static Queue<Integer> que;

    public static void main(String[] args) throws IOException {
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(input.readLine());

        T = Integer.parseInt(st.nextToken());

        for (int tc = 0; tc < T; tc++) {
            st = new StringTokenizer(input.readLine());

            N = Integer.parseInt(st.nextToken());
            K = Integer.parseInt(st.nextToken());

            st = new StringTokenizer(input.readLine());

            delays = new int[N + 1];

            for (int i = 1; i < N + 1; i++) {
                delays[i] = Integer.parseInt(st.nextToken());
            }

            arr = new LinkedList<>();

            count = new int[N + 1];

            for (int i = 0; i < N + 1; i++) {
                List<Integer> lst = new LinkedList<>();

                arr.add(lst);
            }

            for (int k = 0; k < K; k++) {
                st = new StringTokenizer(input.readLine());

                X = Integer.parseInt(st.nextToken());
                Y = Integer.parseInt(st.nextToken());

                arr.get(X).add(Y);

                count[Y] += 1;
            }

            W = Integer.parseInt(input.readLine());

            que = new LinkedList<>();

            dp = new int[N + 1];

            for (int i = 1; i < N + 1; i++) {
                if (count[i] == 0) {
                    que.add(i);
                    dp[i] = delays[i];
                }
            }

            while (!que.isEmpty()) {
                int now = que.poll();

                for (int next : arr.get(now)) {
                    count[next] -= 1;
                    dp[next] = Math.max(dp[now] + delays[next], dp[next]);

                    if (count[next] == 0) {
                        que.add(next);
                    }
                }
            }

            System.out.println(dp[W]);
        }
    }
}