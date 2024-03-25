const fs = require("fs");

// 로컬용
// const [n, input] = fs.readFileSync("./input.txt", "utf-8").toString().trim().split("\n");
const [n, input] = fs.readFileSync("/dev/stdin", "utf-8").toString().trim().split("\n");

// const input = fs.readFileSync("./input.txt", "utf-8").toString().trim().split(/\r?\n/);
// const input = inputLines.map((line) => line.split(" "));

// 백준 제출용
// const input = fs.readFileSync("/dev/stdin", "utf-8").toString().trim().split(/\r?\n/);
// const input = inputLines.map((line) => line.split(" "));


const solution = () => {
  var arr = Array.from(input.split(' '), (element, index) => Number(element));


  var dp = new Array(Number(n)).fill(0);

  dp[0] = Number(arr[0])

  for (let i = 1 ; i < n ;  i ++) {
    for (let j = 0 ; j < i ; j ++) {
      if (arr[j] < arr[i]) {
        dp[i] = Math.max(dp[i], dp[j] + arr[i])
      } else {
        dp[i] = Math.max(dp[i], arr[i])
      }
    }
  }

  const ans = Math.max(...dp);

  console.log(ans)
}

solution();