var hello = "Hello World!";
//alert("Hello World!");
console.log("Hello World!");
a = [100, 50, 20, 120, 10];

function print3Ways() {
    alert("Hello!");
    console.log("This is good for debugging");
    document.write("<h>hello world!</h>");
}

function sumArray() {
    var total = 0;
    for (let i = 0; i < a.length; i++) {
        total += a[i];
    }
    return total;
}

function findMin() {
    var min = a[0];
    for(let i=1;i<a.length;i++) {
        if (a[i] < min) {
            min=a[i];
        }
    }
    return min;
}

function findMax() {
    var max = a[0];
    for(let i=1;i<a.length;i++) {
        if (a[i] > max) {
            max=a[i];
        }
    }
    return max;
}

function funWithArrays() {
    document.write(sumArray() + "<br>");  //br is html element for break
    document.write(findMin() + "<br>");
    document.write(findMax() + "<br>");
}

function plainOldFunction(a="hello world"){
    console.log("this is a plain old function" + a);

    nestedFunction();

    function nestedFunction(){
        console.log("this is a nested function")
    }

    const nestedFunctionExpression = function(){
        console.log("this is a nested function expression");
    }
    nestedFunctionExpression();

}


function firstFunction(callbackFunction = function(){
    console.log("this is the default callback function")}){
    
    callbackFunction();
}


function soManyFunctions(){
    plainOldFunction("hello ted");

    function callback(){
        console.log("this is the callback function");
    }
    firstFunction(callback);
    firstFunction();

}

const obj = {name: "boomer",
            pet_type: "dog",
            cute: true,
            age: 8,
            speak: function(){console.log("woof");}
        
        }
        console.log("my dogs name is" + obj.name);
        obj.speak();