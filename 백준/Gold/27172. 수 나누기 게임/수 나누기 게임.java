import java.util.*;
import java.io.*;

public class Main {
    private static int N;
    private static int[] arr;
    private static boolean[] idx;
    private static int[] score;
    public static void main(String[] args) throws IOException {
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(input.readLine());

        StringTokenizer st = new StringTokenizer(input.readLine());

        arr = new int[N];

        int maxNum = 0;

        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());

            maxNum = Math.max(maxNum, arr[i]);
        }

        idx = new boolean[maxNum + 1];

        for (int num : arr) {
            idx[num] = true;
        }

        score = new int[maxNum + 1];

        for (int num : arr) {
            for (int j = num + num; j < maxNum + 1; j += num) {
                if (idx[j]) {
                    score[num]++;
                    score[j]--;
                }
            }
        }


        StringBuilder sb = new StringBuilder();

        for (int num : arr) {
            sb.append(score[num]).append(" ");
        }

        System.out.println(sb);
    }
}