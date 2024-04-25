import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    private static int N, M;
    private static List<List<Integer>> arr;
    private static int[] inDegree;
    private static Queue<Integer> que;

    public static void main(String[] args) throws IOException {
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(input.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        arr = new ArrayList<>();

        for (int i = 0; i < N + 1; i++) {
            arr.add(new ArrayList<>());
        }

        inDegree = new int[N + 1];

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(input.readLine());

            int A = Integer.parseInt(st.nextToken());
            int B = Integer.parseInt(st.nextToken());

            arr.get(A).add(B);

            inDegree[B]++;
        }

        que = new LinkedList<>();

        for (int i = 1; i < N + 1; i++) {
            if (inDegree[i] == 0) {
                que.add(i);
            }
        }

        StringBuilder sb = new StringBuilder();

        while (!que.isEmpty()) {
            int now = que.poll();

            sb.append(now).append(" ");

            for (int next : arr.get(now)) {
                inDegree[next]--;

                if (inDegree[next] == 0) {
                    que.add(next);
                }
            }
        }

        System.out.println(sb);
    }
}