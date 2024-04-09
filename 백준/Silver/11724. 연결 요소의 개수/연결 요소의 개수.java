import java.io.*;
import java.util.*;

public class Main {

    private static int N;
    private static int M;
    private static List<List<Integer>> arr = new ArrayList<>();

    private static boolean[] visited;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        for (int i = 0; i < N + 1; i++) {
            List<Integer> lst = new ArrayList<>();

            arr.add(lst);
        }

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());

            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());

            arr.get(u).add(v);
            arr.get(v).add(u);
        }

        int ans = 0;

        visited = new boolean[N + 1];

        for (int i = 1; i < N + 1; i++) {
            if (!visited[i]) {
                bfs(i);
                ans++;
            }
        }

        System.out.println(ans);
    }

    static void bfs(int node) {

        Queue<Integer> que = new LinkedList<>();
        que.add(node);

        while (!que.isEmpty()) {
            int now = que.poll();

            for (Integer next : arr.get(now)) {
                if (!visited[next]) {
                    que.add(next);
                    visited[next] = true;
                }
            }
        }
    }
}