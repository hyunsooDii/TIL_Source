var human = {
    name: "김상형",
    age: 29,
    score1: 99,
    score2: 88,
    score3: 77
};

for(var i=1; i<=3; i++){
    console.log(i + "학년 성적= "+ human["score"+i]+"점");
}