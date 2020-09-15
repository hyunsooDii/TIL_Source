function outcount(interval){
    var count = 0;

    var id = setInterval(()=>{ // setInterval(function() <- 람다함수를이용해서 줄일 수 있다.
        count ++;
        if(count == 20){
            clearInterval(id);
        }
        console.log(count + "초 지났습니다.");
    }, interval);
}

outcount(5);
