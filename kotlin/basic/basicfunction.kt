package basic

// fun 함수명(변수명 : 데이터타입, ...) : 리턴타입 { return; }
fun funByReturn(s: String): Any? {
    return s + "-를 입력받았습니다."
}

fun funByParameter(i: Int, s: String) { // Unit (C언어의 Void)
    println (i.toString() + s)
}

fun funByInline(i: Int, i1: Int) = i * i1 // 1줄 짜리일 때 가능

fun funByNoParam() {
    println ("매개변수 없어요")
}

// 함수를 정의한 변수
val funcVariable = { s : String -> println (s)} // -> : 람다 함수(매개변수 -> 함수)
var funVarByType : (String) -> Any? = ::funByReturn // :: : 메소드가 아닌 일반 함수(전역함수를 말함)
                                                    // C++의 함수 포인터와 같음
                                                    // 매개변수로 리턴타입이 한개이고 리턴타입이 ANY인거
fun main(args : Array<String>){
    funByNoParam()
    funByParameter(3, " 숫자입니다")
    println (funByReturn("3을 넘기니"))
    println(funByInline(3, 10))

    funcVariable ("함수형 변수 1")
    println(funVarByType("함수형 변수 2"))
}
