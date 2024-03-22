function solution(nums) {
    var answer = 0;
    
    const N = nums.length / 2;
    
    const num = new Set(nums);
    
    const n = num.size;

    
    if (N < n) {
        answer = N
    } else {
        answer = n
    }
    
    return answer;
}