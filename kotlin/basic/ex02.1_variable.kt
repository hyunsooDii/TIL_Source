fun valTest() {
// val은 const와 같은 읽기전용값임.
val num = 1
val name : String
name = ""

// 에러임. 이미 할당한 값을 재할당 못함.
// msg = "저장"

}
fun main(args : Array<String>){
    // 변수를 정의하는 방법은 2가지
    // "var, val" 구분해야함.
    varTest() // R/W 가능변수
    valTest() // ReadOnly 변수
}