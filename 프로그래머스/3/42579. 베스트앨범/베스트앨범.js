function solution(genres, plays) {
    
  var myMap = new Map();
  
  // Map 생성, 장르를 key로 갖고 재생 시간과 고유번호를 갖는 value
  for (let i = 0; i < genres.length; i++) {
      if (!myMap.get(genres[i])) {
          myMap.set(genres[i], [[plays[i], i]])
      } else {
          myMap.get(genres[i]).push([plays[i], i])
      }
  }
            
  // 같은 key 안에서 큰 값이 앞으로 오도록 정렬
  for (let [key, value] of myMap) {
      value.sort((a, b) => {
          if (a[0] < b[0]) {
              return 1
          } else {
              if (a[0] == b[0] && a[1] > b[1]) {
                  return 1
              }
              return -1
          }
      })
  }
    
  // 전체 합이 큰 순으로 Map 객체 정렬
  const arr = [...myMap];
  
  arr.sort((a, b) => {
      if (a[1].reduce((prev, val) => prev + val[0], 0) < b[1].reduce((prev, val) => prev + val[0], 0)) {
          return 1
      } else {
          return -1
      }
  })
  
  var myMap = new Map(arr);
        
  var answer = [];
  
  // 전체 Map 객체 중에서
  for (let [key, value] of myMap) {
      // 각 객체 당 2개까지만 사용
      for (let i = 0; i < 2; i ++) {
          // 2개 이하인 경우를 위해 사용
          if (value[i]) {
              answer.push(value[i][1])
          }
      }
  }
  
  return answer;
}