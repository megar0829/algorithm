import java.awt.*;
import java.io.*;
import java.util.*;

public class Main {

    private static int N;
    private static int M;
    private static char[][] arr;

    private static int x, y;

    private static int cnt;

    public static void main(String[] args) throws IOException {
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(input.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        arr = new char[N][M];



        for (int i = 0; i < N; i++) {
            String str = input.readLine();

            for (int j = 0; j < str.length(); j++) {
                arr[i][j] = str.charAt(j);

                if (arr[i][j] == 'I') {
                    x = i;
                    y = j;
                }
            }
        }

        int result = bfs(x, y);

        if (result == 0) {
            System.out.println("TT");
        } else {
            System.out.println(result);
        }
    }

    static int bfs(int r, int c) {
        Point[] direction = new Point[]{new Point(-1, 0), new Point(1, 0), new Point(0, -1), new Point(0, 1)};

        boolean[][] visited = new boolean[N][M];

        visited[r][c] = true;

        Queue<Point> que = new LinkedList<>();

        que.add(new Point(r, c));

        while (!que.isEmpty()) {
            Point now = que.poll();

            for (Point d : direction) {
                int ni = now.x + d.x;
                int nj = now.y + d.y;

                if (0 <= ni && ni < N && 0 <= nj && nj < M && !visited[ni][nj]) {
                    if (arr[ni][nj] != 'X') {
                        que.add(new Point(ni, nj));
                        visited[ni][nj] = true;

                        if (arr[ni][nj] == 'P') {
                            cnt++;
                        }
                    }
                }
            }
        }
        return cnt;
    }
}