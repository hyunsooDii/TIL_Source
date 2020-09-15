function sum(n=100){
    var s = 0;
    for (var i=0; i<=n; i++){
        s+=i;
    }
    return s;
}

console.log("1~10 = " + sum(10));
console.log("1~100 = " + sum())