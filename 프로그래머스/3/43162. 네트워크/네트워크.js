function solution(n, computers) {
    var answer = 0;
    
    var visited = new Array(n).fill(false);
    
    const bfs = (idx) => {
        var que = [idx];
        visited[idx] = true;
        
        while (que.length) {
            const now = que.splice(0, 1);
            for (let next in computers[now]) {
                if (computers[now][next] && !visited[next]) {
                    visited[next] = true;
                    que.push(next);
                }
            }
        }
    }
    
    for (let i = 0; i < n; i++) {
        if (!visited[i]) {
            bfs(i);
            answer ++;
        }
    }
    
    return answer;
}