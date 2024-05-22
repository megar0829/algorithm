import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    private static int N, M;
    private static String word;
    private static String S;

    public static void main(String[] args) throws IOException {
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(input.readLine());
        M = Integer.parseInt(input.readLine());
        word = input.readLine();

        int result = 0;
        int count = 0;

        int i = 1;

        while (i < M - 1) {
            if(word.charAt(i - 1) == 'I'
                    && word.charAt(i) == 'O'
                    && word.charAt(i + 1) == 'I')
            {
                count++;

                if(count == N) {
                    count--;
                    result++;
                }

                i++;
            } else {
                count = 0;
            }

            i++;
        }

        System.out.println(result);
    }
}