var hello = "hello world";
alert("Hello world");

a = [100,50,20,120,10];

function print3ways(){
    alert("Hello");
    console.log("this is how you debug");
    document.write("hello world");
}

function funWithArrays(){
    document.write(sumArray() + "<br>");
}

function sumArray(){
    var total = 0;
    for(let i = 0; i<a.length; i++){
        total += a[i];
    }
    return total;
}