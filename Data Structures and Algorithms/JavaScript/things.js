//some things to note with js

// || returns left if the left value can be converted to true and right if otherwise
console.log(null || "user");
console.log("agnes" || "user");

// && returns left if the value can be converted to false and right if otherwise
console.log(null && "user");
console.log("agnes" && "user");

console.log(Number.isNaN(5));

let power = function(base, exponent) {
    let result = 1;
    for (let count = 0; count < exponent; count++){
        result *= base;
    }
    return result;
}

console.log(power(2, 10));

// apparently you can call a function in javascript above its declaration

helloWorld();

function helloWorld() {
  console.log("Hello, world!");
}



// arrow functions

const pow = (base, exponent) => {
    let result = 1;
    for (let count = 0; count < exponent; count++){
        result *= base;
    }
    return result;
}

console.log(pow(2, 10));

function poww(base, exponent){
    if (exponent == 0){
        return 1;
    }
    else{
        return base * poww(base, exponent - 1);
    }
}

let day1 = {
    squirrel: false, 
    events: ["work", "touched tree", "pizza", "running"]
};

console.log(typeof day1);
console.log(day1.wolf);
console.log(day1.events);
console.log(day1);
console.log(Object.keys(day1));

let objectA = {a: 1, b: 2};
console.log(objectA);
console.log(objectA.a);
Object.assign(objectA, {b: 3, c:4});
console.log(objectA);
console.log("coconuts".indexOf("o"));

// rest

function max(...numbers) {
    let result = -Infinity;
    for (let number of numbers){
        if (number > result) result = number;
    }
    return result;
}

console.log(max(5, 3, 4, 5, 0, 2));
let words = ['always', 'understand'];

console.log("will", ...words, "it");

// spread 

arr1 = [2, 3, 4, 6];
arr2 = [...arr1];
console.log(arr2);

arr3 = [1, 2, 3, 4];
arr4 = [5, 6, 7, 8];
arr5 = [...arr3, ...arr4];
console.log(arr5);


let multi = (x, y, z) => {
    return x * y * z;
}

arr6 = [1, 2, 3];
console.log(multi(...arr6));


// math object
function randomPointOnCircle(radius) {
    let angle = Math.random() * 2 * Math.PI;
    return {x: radius * Math.cos(angle), y: radius * Math.sin(angle)};
}

console.log(randomPointOnCircle(5));

function repeat(n, action) {
    for (let i = 0; i < n; i++){
        action(i);
    }
}

repeat(3, console.log);


let labels = [];

repeat(5, (i)=> {
    labels.push(`Unit ${i + 1}`);
})

console.log(labels);

function reduce(array, combine, start) {
    let current = start;
    for (let element of array) {
        current = combine(current, element);
    }
    return current;
}

console.log(reduce([1, 2, 3, 4], (a, b) => a + b, 0));

// standard reduce method
console.log([1, 2, 3, 4].reduce((a, b) => a + b));

// oop 
class Matrix {
    constructor(width, height, element = (x, y) => undefined) {
        this.width = width;
        this.height = height;
        this.content = [];

        for (let y = 0; y < height; y++) {
            for (let x = 0; x < width; x++){
                this.content[y * width + x] = element(x, y);
            }
        }
    }

    get(x, y){
        return this.content[y * this.width + x];
    }
    set(x, y, value){
        this.content[y * this.width + x] = value;
    }
}

// strict mode
function canYouSpotTheProblem() {
    "use strict";

    for (let counter = 0; counter < 10; counter++){
        console.log("Happy runs");
    }
}

canYouSpotTheProblem();

function promptDirection(question){
    let result = prompt(question);

    if (result.toLowerCase() == 'left') return "L";
    if (result.toLowerCase() == 'right') return "R";

    throw new Error("Invalid direction: " + result);
}

function look() {
    if (promptDirection("Which way?") == "L"){
        return "a house";
    }
    else {
        return "two angry bears";
    }
}

try {
    console.log("You see", look());
} catch(error) {
    console.log("Something went wrong: " + error);
}