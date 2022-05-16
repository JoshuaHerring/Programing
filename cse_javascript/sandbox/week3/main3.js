// you can hoist a decleration syntax
function square(number){
    return number * number;
}

function show(iteam){
    console.log (iteam);
}
let number = 4
number = square(number);

show(number);

document.querySelector('#result').textContent = number;


//expression syntax for function cannot be hoisted

let add = function(num1, num2){
    return num1 + num2;
}


document.querySelector('#result').textContent = add(2,3);


// arrow function is efficient but cant be hoisted

let sum = (no1, no2) => (no1 + no2);

document.querySelector('#result').textContent = sum(8,2);


const steps = ["one", "two", "three"];

function makeList(iteam)
{
    const listElement = document.getElementById("myList");
    listElement.innerHTML += `<li>${iteam}</li>`;


}

steps.forEach(makeList);

const buttonElement = document.getElementById("submitButton");

function copyInput()
{
    const inputElement = document.getElementById("inputBox");
    //let outputElement = document.getElementById("output");
    outputElement.innerHTML = inputElement.value;
}

buttonElement.addEventListener("click", copyInput);

const imgElement = document.getElementById("doggo");

function sayYay()
{
    const outputElement = document.getElementById("output")
    outputElement.innerHTML = "Yay"
}

imgElement.addEventListener("click", sayYay )