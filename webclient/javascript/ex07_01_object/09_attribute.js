var person = {
    name : "홍길동",
    eat : function(food){
        console.log(this.name + "이 " + food + "를 먹습니다.");
    }
}

person.eat("피자");