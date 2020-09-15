var student = { };

student.name = "홍길동";
student.hobby = "악기";
student.special = "프로그래밍";
student.department = "생명공학과";

console.log(student)

student.toString = function(){
    for(var key in this){
        if (key != 'toString'){
            console.log(key + '\t' + this[key])
        }
    }
}
delete student.hobby;

student.toString();

for(let key in student){ // for in - 배열이면 요소를 접근하는 index, 객체이면 요소를 접근하는 속성명을 key에 저장
    console.log(key, student[key])
}

console.log('name' in student);
console.log('성별' in student);