var korean = "82점";
var english = "75점";
// var total = Number(korean) + Number(english); // Number형식으로 형변환
var total = parseInt(korean) + parseInt(english); // parse형 함수 = 숫자 이외의 값이 포함되어 있으면 숫자 부분만 해석
console.log("총점은 " + total + "이다.");

