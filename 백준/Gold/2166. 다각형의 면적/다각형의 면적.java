import java.awt.*;
import java.io.*;
import java.util.*;

public class Main {
    private static int N;
    public static void main(String[] args) throws IOException {
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(input.readLine());

        long[] xPoints = new long[N + 1];
        long[] yPoints = new long[N + 1];

        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(input.readLine());

            xPoints[i] = Integer.parseInt(st.nextToken());
            yPoints[i] = Integer.parseInt(st.nextToken());
        }

        xPoints[N] = xPoints[0];
        yPoints[N] = yPoints[0];

        long left = 0;
        long right = 0;

        for (int i = 0; i < N; i++) {
            left += xPoints[i] * yPoints[i + 1];
            right += xPoints[i + 1] * yPoints[i];
        }

        String area = String.format("%.1f", (Math.abs(left - right) / 2.0));

        System.out.println(area);
    }
}