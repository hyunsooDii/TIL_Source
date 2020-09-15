var add = function(a,b){
    return a+b;
}

var multi = function(a,b){
    return a*b;
}

function calc(a, b, f){
    return f(a,b);
}

console.log("2 + 3 = " + calc(2,3,add));
console.log("2 * 3 = " + calc(2,3,multi));

console.log("2 + 3 = " + calc(2,3,(a,b)=>a+b)); // PYTHON에서의 람다함수, 화살표함수라고 부름
console.log("2 * 3 = " + calc(2,3,(a,b)=>a*b));

