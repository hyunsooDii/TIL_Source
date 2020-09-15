/*
자바스트립트에서는 컴파일 할 때 식별자부터 찾은 후 명령을 실행하기 때문에 
먼저 식별자를 선언해도 컴파일이 가능 - hoisting 
*/
var global = "전역"; 

func(); // 식별자를 먼저 선언해도 실행이 된다

function func(){
    local = "로컬"; // 전역변수
    console.log("함수안 local = " + local);
    console.log("함수안 global = " + global);
}


console.log("함수밖 local = " + local);
console.log("함수밖 global = " + global);
