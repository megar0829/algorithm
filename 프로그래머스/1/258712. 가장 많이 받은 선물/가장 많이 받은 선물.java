import java.util.*;

class Solution {

    private int N;

    public int solution(String[] friends, String[] gifts) {
        N = friends.length;

        int[][] giftIndex = new int[N][N];

//        Arrays.fill(giftIndex, 1);

        List<String> lst = new ArrayList<>();

        for (String s : friends) {
            lst.add(s);
        }

        for (int i = 0; i < gifts.length; i++) {
            String[] str = gifts[i].split(" ");
            String a = str[0];
            String b = str[1];

            giftIndex[lst.indexOf(a)][lst.indexOf(b)]++;
            giftIndex[lst.indexOf(b)][lst.indexOf(a)]--;
        }

        int[] sumGift = new int[N];

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                sumGift[i] += giftIndex[i][j];
            }
        }

        int[] result = new int[N];

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (i != j) {
                    if (giftIndex[i][j] == 0) {
                        if (sumGift[i] > sumGift[j]) {
                            result[i]++;
                        }
                    } else {
                        if (giftIndex[i][j] > 0) {
                            result[i]++;
                        }
                    }
                }
            }
        }
        
        int answer = 0;

        for (int i = 0; i < N; i++) {
            if (result[i] > answer) {
                answer = result[i];
            }
        }

        return answer;
    }
}