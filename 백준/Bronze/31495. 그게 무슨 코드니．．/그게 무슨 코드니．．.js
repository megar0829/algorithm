const fs = require("fs");

// 로컬용
// const input = fs.readFileSync("./input.txt", "utf-8").toString().trim().split(/\r?\n/);
// const input = inputLines.map((line) => line.split(" "));

// 백준 제출용
const input = fs.readFileSync("/dev/stdin", "utf-8").toString().trim().split(/\r?\n/);
// const input = inputLines.map((line) => line.split(" "));


const solution = () => {
  const endIndex = input[0].length;

  if (input[0][0] == '"' && input[0][endIndex - 1] == '"') {
    ans = input[0].slice(1, -1);

    if (!ans) {
      console.log("CE");
      return
    }

    console.log(ans);
    return
  } else {
    console.log("CE");
    return
  }
}

solution();