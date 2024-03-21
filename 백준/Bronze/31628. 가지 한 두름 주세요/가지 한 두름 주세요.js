const fs = require("fs");

// 로컬용
// const inputLines = fs.readFileSync("./input.txt", "utf-8").toString().trim().split(/\r?\n/);
// const input = inputLines.map((line) => line.split(" "));

// 백준 제출용
const inputLines = fs.readFileSync("/dev/stdin", "utf-8").toString().trim().split(/\r?\n/);
const input = inputLines.map((line) => line.split(" "));

const check = (lst) => {
  const val = lst[0];

  for (let i = 1; i < 10; i++) {
    if (lst[i] != val) {
      return false
    }
  }
  return true
}


const solution = () => {
  for (let i = 0; i < 10; i++) {
    if (check(input[i])) {
      console.log(1);
      return
    }

    const save_lst = [];

    for (let j = 0; j < 10; j ++) {
      save_lst.push(input[j][i]);
    }

    if (check(save_lst)) {
      console.log(1);
      return
    }
  }
  console.log(0);
  return
}

solution();