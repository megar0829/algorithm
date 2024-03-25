function solution(participant, completion) {
    var myMap = new Map();
    
    for (const part of participant) {
        if (!myMap.get(part)) {
            myMap.set(part, 1)
        } else {
            myMap.set(part, myMap.get(part) + 1)
        }
    }
    
    for (const comple of completion) {
        myMap.set(comple, myMap.get(comple) - 1)
    }
    
    var answer = '';
    
    for (const part of participant) {
        if (myMap.get(part)) {
            answer = part;
            break
        }
    }
    
    
    return answer;
}