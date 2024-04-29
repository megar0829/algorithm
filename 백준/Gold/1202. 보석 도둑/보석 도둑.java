import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {
    private static int N, K;
    private static PriorityQueue<Node1> jems;
    private static int[] bags;
    private static PriorityQueue<Integer> pq;

    public static void main(String[] args) throws IOException {
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(input.readLine());

        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        jems = new PriorityQueue<>();

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(input.readLine());

            int M = Integer.parseInt(st.nextToken());
            int V = Integer.parseInt(st.nextToken());

            jems.add(new Node1(M, V));
        }

        bags = new int[K];

        for (int i = 0; i < K; i++) {
            bags[i] = Integer.parseInt(input.readLine());
        }

        Arrays.sort(bags);

        long ans = 0;

        pq = new PriorityQueue<>();

        for (int bag : bags) {
            while (!jems.isEmpty() && (bag >= jems.peek().M)) {
                pq.add(-jems.poll().V);
            }

            if (!pq.isEmpty()) {
                ans -= pq.poll();
            }
        }

        System.out.println(ans);
    }

}


class Node1 implements Comparable<Node1> {
    int M;
    int V;

    public Node1(int m, int v) {
        this.M = m;
        this.V = v;
    }

    @Override
    public int compareTo(Node1 o) {
        return this.M  - o.M;
    }
}