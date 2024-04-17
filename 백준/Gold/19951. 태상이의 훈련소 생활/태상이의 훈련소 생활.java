import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    private static int N, M;
    private static int[] arr;
    private static int[] cost;

    public static void main(String[] args) throws IOException {
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(input.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        arr = new int[N];

        st = new StringTokenizer(input.readLine());

        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        cost = new int[N + 1];

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(input.readLine());

            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int k = Integer.parseInt(st.nextToken());

            cost[a - 1] += k;
            cost[b] -= k;
        }

        int sumVal = cost[0];

        arr[0] += sumVal;

        for (int i = 1; i < N; i++) {
            sumVal += cost[i];
            arr[i] += sumVal;
        }

        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < N; i++) {
            sb.append(arr[i]).append(" ");
        }

        System.out.println(sb);
    }
}