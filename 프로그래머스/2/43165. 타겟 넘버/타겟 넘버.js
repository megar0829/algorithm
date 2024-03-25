function solution(numbers, target) {
    var answer = 0;
    
    function dfs(idx, sumVal) {
        if (idx == numbers.length) {
            if (sumVal == target) {
                answer ++;
            }
            return
        }
        
        dfs(idx + 1, sumVal + numbers[idx]);
        dfs(idx + 1, sumVal - numbers[idx]);
    }
    
    dfs(0, 0);
    
    return answer;
}