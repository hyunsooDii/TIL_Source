function func(){
    if(true)
        throw "예외가 발생했습니다."; // 강제로 예외를 발생시키는 명령어
}

try{
    func();
} catch(exception){
    console.log(exception);
    }
    
console.log("실행을 완료하였습니다.")