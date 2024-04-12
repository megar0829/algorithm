import java.io.*;
import java.util.*;

class Solution {
    private static int N;
    private static boolean[] used;
    private static int targetVal;
    private static int answer;
    private static int[] arr;
    
    
    public int solution(int[] numbers, int target) {
        N = numbers.length;
        
        used = new boolean[N];
        
        targetVal = target;
        
        arr = new int[N];
        
        for (int i = 0; i < N; i++) {
            arr[i] = numbers[i];
        }
        
        answer = 0;
        
        dfs(0, 0);
        
        return answer;
    }
    
    static void dfs(int idx, int sumVal) {
        if (idx == N) {
            if (sumVal == targetVal) {
                answer ++;
            }
            
            return;
        }
        
        dfs(idx + 1, sumVal + arr[idx]);
        dfs(idx + 1, sumVal - arr[idx]);
    }
}