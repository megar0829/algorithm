import java.io.*;
import java.util.*;

class Item {
    int weight;
    int value;

    Item (int W, int V) {
        this.weight = W;
        this.value = V;
    }
}
public class Main {
    private static int N, K;
    private static int[][] dp;

    public static void main(String[] args) throws IOException {
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(input.readLine());

        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        List<Item> arr = new ArrayList<>();

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(input.readLine());

            int w, v;

            w = Integer.parseInt(st.nextToken());
            v = Integer.parseInt(st.nextToken());

            arr.add(new Item(w, v));
        }

        dp = new int[N + 1][K + 1];

        for (int i = 1; i < N + 1; i++) {
            Item item = arr.get(i - 1);

            for (int j = 1; j < K + 1; j++) {
                if (j < item.weight) {
                    dp[i][j] = dp[i - 1][j];
                }
                else {
                    dp[i][j] = Math.max(item.value + dp[i - 1][j - item.weight], dp[i - 1][j]);
                }
            }
        }

        System.out.println(dp[N][K]);
    }
}