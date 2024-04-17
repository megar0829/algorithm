import java.util.*;
import java.io.*;


class Edge implements Comparable<Edge> {
    int from, to, cost;

    Edge(int from, int to, int cost) {
        this.from = from;
        this.to = to;
        this.cost = cost;
    }

    @Override
    public int compareTo(Edge o) {
        return cost - o.cost;
    }
}

public class Main {

    /**
     * 노드 : N, 양방향 간선 : M
     *
     */

    private static int N, M;
    private static PriorityQueue<Edge> edge;
    private static int[] parent;

    public static void main(String[] args) throws IOException {
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(input.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        edge = new PriorityQueue<>();

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(input.readLine());

            int f = Integer.parseInt(st.nextToken());
            int t = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());

            edge.add(new Edge(f, t, c));
        }

        parent = new int[N + 1];

        for (int i = 0; i < N + 1; i++) {
            parent[i] = i;
        }


        int ans = 0;
        int maxValue = 0;

        for (int i = 0; i < M; i++) {
            Edge now = edge.poll();

            int x = findSet(now.from);
            int y = findSet(now.to);

            if (x != y) {
                ans += now.cost;
                union(x, y);

                maxValue = now.cost;
            }
        }

        System.out.println(ans - maxValue);
    }

    static int findSet(int x) {
        if (parent[x] == x) {
            return x;
        }

        parent[x] = findSet(parent[x]);

        return parent[x];
    }

    static void union(int x, int y) {
        if (x > y) {
            parent[x] = y;
        } else {
            parent[y] = x;
        }
    }
}