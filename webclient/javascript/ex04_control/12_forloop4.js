var arScore = [88, 78, 96, 54, 23];

var sum = 0;

for(var st = 0; st < arScore.length; st++){
    sum += arScore[st];
}

console.log("총점 : " + sum + ",평균 : " + sum/arScore.length);
console.log(`총점 : ${sum}, 평균 : ${sum/arScore.length}`); // Formating 