function solution(maps) {    
    const N = maps.length;
    const M = maps[0].length;
        
    var visited = Array.from(
        {length: N}, 
        () => Array(M).fill(0)
    );
    
    var answer = 0;
    
    const bfs = () => {
        var que = [[0, 0]];
        visited[0][0] = 1
        
        while (que.length) {
            var [x, y] = que.splice(0, 1)[0];
            
            for (let [dx, dy] of [[-1, 0], [1, 0], [0, -1], [0, 1]]) {
                var [nx, ny] = [x + dx, y + dy];
                
                if (0 <= nx && nx < N && 0 <= ny && ny < M) {
                  if (maps[nx][ny] && !visited[nx][ny]) {
                        que.push([nx, ny]);
                        visited[nx][ny] = visited[x][y] + 1;
                    }
                }
            }
        }
        
        
        if (!visited[N - 1][M - 1]) {
            return -1
        }
        return visited[N - 1][M - 1]
    }
    
    answer = bfs();
    
    return answer;
}