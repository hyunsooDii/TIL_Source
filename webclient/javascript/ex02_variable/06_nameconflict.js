var score = 100;

function func(){
    var score = 77;
    console.log("함수 안 score = " + score);
}
func();

console.log("함수 밖 score = " + score);