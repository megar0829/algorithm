import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.StringTokenizer;

public class Main {

    private static int T;
    private static int n;
    private static int[] arrA;
    private static int m;
    private static int[] arrB;

    private static List<Integer> sumA, sumB;

    public static void main(String[] args) throws IOException {
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));

        T = Integer.parseInt(input.readLine());

        n = Integer.parseInt(input.readLine());

        arrA = new int[n];

        StringTokenizer st = new StringTokenizer(input.readLine());

        for (int i = 0; i < n; i++) {
            arrA[i] = Integer.parseInt(st.nextToken());
        }

        m = Integer.parseInt(input.readLine());

        arrB = new int[m];

        st = new StringTokenizer(input.readLine());

        for (int i = 0; i < m; i++) {
            arrB[i] = Integer.parseInt(st.nextToken());
        }

        sumA = new ArrayList<>();

        int saveSum;

        for (int i = 0; i < n; i++) {
            saveSum = 0;

            for (int j = i; j < n; j++) {
                saveSum += arrA[j];
                sumA.add(saveSum);
            }
        }

        sumB = new ArrayList<>();

        for (int i = 0; i < m; i++) {
            saveSum = 0;

            for (int j = i; j < m; j++) {
                saveSum += arrB[j];
                sumB.add(saveSum);
            }
        }

        sumA.sort(null);
        sumB.sort(null);

        int idxA = 0;
        int idxB = sumB.size() - 1;

        int sumVal;

        long cnt = 0;

        while (idxA < sumA.size() && idxB >= 0) {
            sumVal = sumA.get(idxA) + sumB.get(idxB);

            if (sumVal == T) {
                long a = sumA.get(idxA);
                long b = sumB.get(idxB);
                long cntA = 0;
                long cntB = 0;

                while (idxA < sumA.size() && sumA.get(idxA) == a) {
                    cntA++;
                    idxA++;
                }

                while (idxB >= 0 && sumB.get(idxB) == b) {
                    cntB++;
                    idxB--;
                }

                cnt += cntA * cntB;
            } else if (sumVal > T) {
                idxB--;
            } else if (sumVal < T) {
                idxA++;
            }
        }

        System.out.println(cnt);
    }
}