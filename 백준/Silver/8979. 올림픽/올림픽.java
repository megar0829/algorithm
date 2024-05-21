import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    private static int N, K;
    private static List<Country> arr;
    private static int[] grade;

    public static void main(String[] args) throws IOException {
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(input.readLine());

        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        arr = new ArrayList<>();

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(input.readLine());

            arr.add(new Country(
                Integer.parseInt(st.nextToken()),
                Integer.parseInt(st.nextToken()),
                Integer.parseInt(st.nextToken()),
                Integer.parseInt(st.nextToken())
            ));
        }

        Collections.sort(arr);

        grade = new int[N];

        int gradeNum = 1;

        grade[0] = gradeNum;

        for (int i = 1; i < N; i++) {
            gradeNum++;

            if (
                    (arr.get(i - 1).gold == arr.get(i).gold)
                    && (arr.get(i - 1).silver == arr.get(i).silver)
                    && (arr.get(i - 1).bronze == arr.get(i).bronze)
            ) {
                grade[i] = grade[i - 1];
            } else {
                grade[i] = gradeNum;
            }
        }
        
        for (int i = 0; i < N; i++) {
            if (arr.get(i).num == K) {
                System.out.println(grade[i]);

                break;
            }
        }
    }

    static class Country implements Comparable<Country> {
        int num;
        int gold;
        int silver;
        int bronze;

        public Country(int num, int gold, int silver, int bronze) {
            this.num = num;
            this.gold = gold;
            this.silver = silver;
            this.bronze = bronze;
        }

        @Override
        public int compareTo(Country o) {
            if (this.gold > o.gold) {
                return -1;
            } else if (this.gold == o.gold) {
                if (this.silver > o.silver) {
                    return -1;
                } else if (this.silver == o.silver) {
                    if (this.bronze > o.bronze) {
                        return -1;
                    } else if (this.bronze == o.bronze) {
                        return 0;
                    } else {
                        return 1;
                    }
                } else {
                    return 1;
                }
            } else {
                return 1;
            }
        }
    }
}