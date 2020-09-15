var human = {
    name: "김상형",
    age: 29,
    intro: function() {
    console.log("name = " + this.name);
    console.log("age = " + this.age);
    },
    toString:function(){
        return "Human" + this.name
    }
    };
    // human.intro();
    console.log(human)