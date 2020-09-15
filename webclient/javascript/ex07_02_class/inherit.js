class Parent{
    constructor(name){
        this.name = name;
    }

    print(){
        console.log("이름 : " + this.name);
    }

    static sayHello(){ // static은 this를 쓸 수 없다
        console.log("Hello~ man");
    }
}

class Child extends Parent{
    constructor(name, age){
        super(name);
        this.age = age;
    }

    print(){
        super.print();
        console.log("나이 : " + this.age) // Override
    }

    static sayHello(){ // static은 this를 쓸 수 없다
        console.log("");
    }
}

class GrandChild extends Child{
    constructor(name, age, address){
        super(name, age);
        this.address = address;
    }
    
    print(){
        super.print();
        console.log("주소 : " + this.address);
    }
    static sayHello(){ // static은 this를 쓸 수 없다
        console.log("Hello~ manmas");
    }
}

var person = new GrandChild("홍길동", 20, "서울");
person.print();
GrandChild.sayHello();