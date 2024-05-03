import java.awt.*;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    private static int n;
    private static Point[] arr;
    private static PriorityQueue<Integer> que;
    private static int d;

    public static void main(String[] args) throws IOException {
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(input.readLine());

        arr = new Point[n];

        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(input.readLine());

            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());

            arr[i] = new Point(Math.min(x, y), Math.max(x, y));
        }

        Comparator<Point> comparator = (o1, o2) -> {
            if (o1.y == o2.y) {
                return o1.x - o2.x;
            }
            return o1.y - o2.y;
        };

        Arrays.sort(arr, comparator);

        d = Integer.parseInt(input.readLine());

        que = new PriorityQueue<>();

        int ans = 0;

        for (Point point : arr) {
            int start = point.x;
            int end = point.y;

            que.add(start);

            int lineStart = end - d;

            while (!que.isEmpty() && que.peek() < lineStart) {
                que.poll();
            }

            ans = Math.max(ans, que.size());
        }

        System.out.println(ans);
    }
}