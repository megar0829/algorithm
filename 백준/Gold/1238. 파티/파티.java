import java.io.*;
import java.util.*;

class Node implements Comparable<Node> {
    int idx;
    int cost;

    @Override
    public String toString() {
        return "Node{" +
                "idx=" + idx +
                ", cost=" + cost +
                '}';
    }

    Node(int idx, int cost) {
        this.idx = idx;
        this.cost = cost;
    }

    @Override
    public int compareTo(Node o) {
        return this.cost - o.cost;
    }
}

public class Main {
    private static int N, M, X;
    private static List<List<Node>> arr;

    private static PriorityQueue<Node> pq;

    private static int[] distance;
    public static void main(String[] args) throws IOException {
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(input.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        X = Integer.parseInt(st.nextToken());

        arr = new ArrayList<>();

        for (int i = 0; i < N + 1; i++) {
            List<Node> lst = new ArrayList<>();
            arr.add(lst);
        }

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(input.readLine());

            int f, t, dist;

            f = Integer.parseInt(st.nextToken());
            t = Integer.parseInt(st.nextToken());
            dist = Integer.parseInt(st.nextToken());

            arr.get(f).add(new Node(t, dist));
        }

        int ans = 0;

        for (int i = 1; i < N + 1; i++) {
            ans = Math.max(ans, dijkstra(i, X) + dijkstra(X, i));
        }

        System.out.println(ans);
    }

    static int dijkstra(int start, int end) {
        distance = new int[N + 1];
        Arrays.fill(distance, Integer.MAX_VALUE);

        pq = new PriorityQueue<>();

        pq.add(new Node(start, 0));

        distance[start] = 0;

        while (!pq.isEmpty()) {
            Node now = pq.poll();

            int node, cost;
            node = now.idx;
            cost = now.cost;

            for (Node next : arr.get(node)) {
                int nextNode, dist;
                nextNode = next.idx;
                dist = next.cost;

                int newCost = cost + dist;

                if (newCost < distance[nextNode]) {
                    distance[nextNode] = newCost;
                    pq.add(new Node(nextNode, newCost));
                }
            }
        }

        return distance[end];
    }
}