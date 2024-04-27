import java.awt.*;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

    private static int N, M;
    private static char[][] arr;
    private static boolean[][] visited;
    private static boolean[][] finished;
    private static int cnt;

    public static void main(String[] args) throws IOException {
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(input.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        arr = new char[N][M];

        for (int i = 0; i < N; i++) {
            String line = input.readLine();

            for (int j = 0; j < M; j++) {
                arr[i][j] = line.charAt(j);
            }
        }

        visited = new boolean[N][M];

        finished = new boolean[N][M];

        cnt = 0;

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (!visited[i][j]) {
                    dfs(i, j);
                }
            }
        }

        System.out.println(cnt);
    }

    private static int nr, nc;

    public static void dfs(int r, int c) {

        visited[r][c] = true;

        char d = arr[r][c];

        if (d == 'U') {
            nr = r - 1;
            nc = c;
        } else if (d == 'D') {
            nr = r + 1;
            nc = c;
        } else if (d == 'L') {
            nr = r;
            nc = c - 1;
        } else {
            nr = r;
            nc = c  + 1;
        }

        if (!visited[nr][nc]) {
            dfs(nr, nc);
        } else {
            if (!finished[nr][nc]) {
                cnt++;
            }
        }

        finished[r][c] = true;
    }
}