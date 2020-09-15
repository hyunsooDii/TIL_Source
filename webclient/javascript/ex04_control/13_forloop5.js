var arScore = [88, 78, 96, 54, 23];

var sum = 0;

for(let ix in arScore){ //for in - index의 배열번호 값을 ix에 넘겨줌  for of - index의 값을 ix에 넘겨줌
    sum += arScore[ix]
}

console.log("총점 : " + sum + ",평균 : " + sum/arScore.length);
console.log(`총점 : ${sum}, 평균 : ${sum/arScore.length}`); // Formating 