import java.io.*;
import java.util.*;

public class Main {

    private static int N, M;
    private static int[] arr;

    private static boolean[] used;

    private static int[] sequence;

    private static StringBuilder sb;

    public static void main(String[] args) throws IOException {
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(input.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        arr = new int[N];

        Set<Integer> intHashSet = new HashSet<>();

        st = new StringTokenizer(input.readLine());

        for (int i = 0; i < N; i++) {
            intHashSet.add(Integer.parseInt(st.nextToken()));
        }

        int idx = 0;

        for (int num : intHashSet) {
            arr[idx] = num;
            idx++;
        }

        Arrays.sort(arr);

        used = new boolean[N];

        sequence = new int[N];

        sb = new StringBuilder();

        dfs(0);

        System.out.println(sb);
    }

    static void dfs(int idx) {
        if (idx == M) {
            for (int i = 0; i < M; i++) {
                sb.append(sequence[i]).append(' ');
            }
            sb.append('\n');
            return;
        }

        for (int i = 0; i < N; i++) {
            if (!used[i]) {
                used[i] = true;
                sequence[idx] = arr[i];
                dfs(idx + 1);
                used[i] = false;
                sequence[idx] = 0;
            }
        }
    }
}