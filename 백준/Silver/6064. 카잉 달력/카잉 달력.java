import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    private static int T;
    private static int M, N, x, y;
    private static int val;
    private static int ans;

    public static void main(String[] args) throws IOException {
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));

        T = Integer.parseInt(input.readLine());

        for (int i = 0; i < T; i++) {
            StringTokenizer st = new StringTokenizer(input.readLine());

            M = Integer.parseInt(st.nextToken());
            N = Integer.parseInt(st.nextToken());
            x = Integer.parseInt(st.nextToken());
            y = Integer.parseInt(st.nextToken());

            val = x;

            ans = -1;

            while (val <= M * N) {
                if (((val - x) % M == 0) && ((val - y) % N == 0)) {
                    ans = val;
                    break;
                }
                val += M;
            }

            System.out.println(ans);
        }
    }
}