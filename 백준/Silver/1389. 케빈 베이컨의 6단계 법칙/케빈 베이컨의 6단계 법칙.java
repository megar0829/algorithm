import java.awt.*;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {
    private static int N, M;
    private static List<List<Integer>> arr;
    private static PriorityQueue<Node> pq;
    private static int ans;
    private static int val;
    private static int[][] distance;

    static class Node implements Comparable<Node> {

        int dist;
        int nowNode;

        public Node(int dist, int nowNode) {
            this.dist = dist;
            this.nowNode = nowNode;
        }

        @Override
        public int compareTo(Node o) {
            return this.dist - o.dist;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(input.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        arr = new ArrayList<>();

        for (int i = 0; i < N + 1; i++) {
            arr.add(new ArrayList<>());
        }

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(input.readLine());

            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            arr.get(a).add(b);
            arr.get(b).add(a);
        }

        ans = 0;
        val = Integer.MAX_VALUE;

        distance = new int[N + 1][N + 1];

        for (int i = 1; i < N; i++) {
            for (int j = i + 1; j < N + 1; j++) {
                int d = dijkstra(i, j);

                distance[i][j] = d;
                distance[j][i] = d;
            }
        }

        for (int i = 1; i < N + 1; i++) {
            int sumVal = 0;

            for (int j = 1; j < N + 1; j++) {
                sumVal += distance[i][j];
            }

            if (sumVal < val) {
                val = sumVal;
                ans = i;
            }
        }

        System.out.println(ans);
    }

    public static int dijkstra(int startNode, int endNode) {
        pq = new PriorityQueue<>();
        pq.add(new Node(0, startNode));

        boolean[] visited = new boolean[N + 1];

        while (!pq.isEmpty()) {
            Node now = pq.poll();

            if (now.nowNode == endNode) {
                return now.dist;
            }

            for (int nextNode : arr.get(now.nowNode)) {
                if (!visited[nextNode]) {
                    visited[nextNode] = true;
                    pq.add(new Node(now.dist + 1, nextNode));
                }
            }
        }

        return 0;
    }
}