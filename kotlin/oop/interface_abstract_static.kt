package oop
interface SimpleInterface{ // SimpleInterface : 타입, 타입의 종류 : 자료형, 클래스, 인터페이스
    fun TestFunc();
}

class SimpleImp : SimpleInterface{ // 구현
    override fun TestFunc() = println ("구현했음");
}

abstract class TestAbstract{
    fun TestFunc() = println("TestFunc");
    abstract fun abstractFunc();
}

class TestAbstractImp : TestAbstract(){ //  상속
    override fun abstractFunc() = println("상속구현했음");

    // companion object {} 안에서 구현해야 static 가능
    companion object { // 내부에서 운영되는 독자적인 객체
    var staticVar = "staticVar";
    fun staticFunc() = println("이거스태틱 함수임");
    }
}

fun main(args : Array<String>){
    // SimpleInterface
    SimpleImp().TestFunc();
    var obj : SimpleInterface;

    // 추상화
    // 아래 코드는 다음과 같이도 가능함
    // TestAbstractImp().apply { TestFunc(); abstractFunc(); }
    var obj2 = TestAbstractImp();
    obj2.TestFunc();
    obj2.abstractFunc();

    // static
    println( TestAbstractImp.staticVar);
    TestAbstractImp.staticFunc() ;
}