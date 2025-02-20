// Question 1
//The Function which does not have function keyword and function name and denoted by => is 
//known as Arrow Function.
//It has a shorter syntax compared to traditional function expression.
// An arrow function in JavaScript is a more concise way to write functions.
//The syntax of an arrow function differs  from a traditional function expression in JavaScript.
// Here’s a clear comparison
//Arrow Function
//Uses the => ("arrow") operator.
// Does not require the function keyword and function name
//syntax
// var refrencevariable=(parameters){
//    statements
//    return;}
// Example for arrow function
var a=(c,b)=>c+b;
// traditional function
var a=function(c,b){
    return a+b;
}
// question 2
var add=(a,b)=>a+b;
console.log(add(2, 3)); 
//Question3
var square=n=>n*n;
console.log(square(2)); 
//Question4
//When an arrow function takes exactly one parameter, parentheses are optional.
// This makes the function shorter in arrow function clear.(shortand syntax)
//Var referenceVariable = parameter =>  return expression; 
//referenceVariable(arguments); 
//example
//var sum=a=>a+a
//Question 5
//Concise body-implicit return,
var cube=num=>num**3;
console.log(cube(2))
//blockbody-explicit return,
var cube=num=>{return num**3}
console.log(cube(2))
//Question 6
var sub=(a,b)=>{
    return b-a
}
console.log(sub(10,20))
//Question 7
var message = () => {
    return "Hello, World"
}
console.log(message())