// 1st Question
function processNumbers(x,y,callback){
    return callback(a,b)
}
var res=processNumbers(3,4,function(a,b){
    return a+b
})
console.log("sum:",res)
    
// 2nd Question
function greet(callback){
    return callback("Alice")
}
var a=greet(function(name){
    return name
});
console.log("Hello,",a)


//3rd Question
function calculate(x,y,callback){
    return callback(x,y)
}
var value=calculate(10,5,function(x,y){
    return x-y
})
console.log("Difference:", value);