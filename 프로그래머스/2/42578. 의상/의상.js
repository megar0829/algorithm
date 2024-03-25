function solution(clothes) {
    var myMap = new Map();
    
    for (const [name, type] of clothes) {
        if (!myMap.get(type)) {
            myMap.set(type, [name])
        } else {
            myMap.get(type).push(name)
        }
    }
    
    var answer = 1;
    
    for (let [key, value] of myMap) {
        answer *= (value.length + 1)
    }

    return answer - 1;
}