/* Lesson 3 */

/* FUNCTIONS */

// Step 1: Using function declaration, define a function named add that takes two arguments, number1 and number2

function add(number1, number2)
{
    
    // Step 2: In the function, return the sum of the parameters number1 and number2
    
    return number1 + number2;
}


// Step 3: Step 3: Using function declaration, define another function named addNumbers that gets the values of two HTML form controls with IDs of addend1 and addend2. Pass them to the add function
function addNumbers() 
{
    let addend1 = parseInt(document.getElementById('addend1').value);
    let addend2 = parseInt(document.getElementById('addend2').value);
    let result = add(addend1, addend2);

    // Step 4: Assign the return value to an HTML form element with an ID of sum

    document.getElementById('sum').value = result;
}


// Step 5: Add a "click" event listener to the HTML button with an ID of addNumbers that calls the addNumbers function

document.getElementById('addNumbers').addEventListener('click', addNumbers);



// Step 6: Using function expressions, repeat Steps 1-5 with new functions named subtract and subtractNumbers and HTML form controls with IDs of minuend, subtrahend, difference and subtractNumbers
let subtract = function(number1, number2)
{
    return number1 - number2;
}

let subtractNumbers = function()
{
    let minuend = parseInt(document.getElementById('minuend').value);
    let subtrahend = parseInt(document.getElementById('subtrahend').value);
    let result = subtract(minuend, subtrahend);

    document.getElementById('difference').value = result;
}

document.getElementById('subtractNumbers').addEventListener('click', subtractNumbers);


// Step 7: Using arrow functions, repeat Steps 1-5 with new functions named multiply and mulitplyNumbers and HTML form controls with IDs of factor1, factor2, product and multiplyNumbers

let multiply = (num1, num2) => num1 * num2;

let multiplyNumbers = () => 
{
    let factor1 = parseInt(document.getElementById('factor1').value);
    let factor2 = parseInt(document.getElementById('factor2').value);
    let result = multiply(factor1, factor2)

    document.getElementById('product').value = result;
}

document.getElementById('multiplyNumbers').addEventListener('click', multiplyNumbers);

// Step 8: Using any of the three function declaration types, repeat Steps 1-5 with new functions named divide and divideNumbers and HTML form controls with IDs of dividend, divisor, quotient and divideNumbers

let divide = (num1, num2) => num1 / num2;

let divideNumbers = () =>
{
    dividend = parseInt(document.getElementById('dividend').value);
    divisor = parseInt(document.getElementById('divisor').value);
    let result = divide(dividend, divisor);

    document.getElementById('quotient').value = result;
}

document.getElementById('divideNumbers').addEventListener('click', divideNumbers);

// Step 9: Test all of the mathematical functionality of the task3.html page.


/* BUILT-IN METHODS */

// Step 1: Declare and instantiate a variable of type Date to hold the current date

let date = new Date();

console.log(date);

// Step 2: Declare a variable to hold the current year

let year = '';

// Step 3: Using the variable declared in Step 1, call the built-in getFullYear() method/function and assign it to the variable declared in Step 2

year = date.getFullYear();

// Step 4: Assign the current year variable to an HTML form element with an ID of year

document.getElementById('year').innerHTML = year;


/* ARRAY METHODS */

// Step 1: Declare and instantiate an array variable to hold the numbers 1 through 25
numbers = [];

for (let i = 1; i <= 25; i++)
{
    numbers[i - 1] = i;
}
console.log(numbers);

// Step 2: Assign the value of the array variable to the HTML element with an ID of "array"
document.getElementById('array').innerHTML = numbers;

// Step 3: Use the filter array method to find all of the odd numbers of the array variable and assign the reult to the HTML element with an ID of "odds" ( hint: % (modulus operartor) )

let odds = numbers.filter(number => number%2)

console.log(odds);

document.getElementById('odds').innerHTML = odds;
// Step 4: Use the filter array method to find all of the even numbers of the array variable and assign the result to the HTML element with an ID of "evens"
let evens = numbers.filter(number => number % 2 == 0);

document.getElementById('evens').innerHTML = evens;
  
console.log(evens);

// Step 5: Use the reduce array method to sum the array variable elements and assign the result to the HTML element with an ID of "sumOfArray"
document.getElementById('sumOfArray').innerHTML = numbers.reduce((total,iteam) => total + iteam);

// Step 6: Use the map array method to multiple each element in the array variable by 2 and assign the result to the HTML element with an ID of "multiplied"
let multiplied = numbers.map(x => x*2);

document.getElementById('multiplied').innerHTML = multiplied;


// Step 7: Use the map and reduce array methods to sum the array elements after multiplying each element by two.  Assign the result to the HTML element with an ID of "sumOfMultiplied"

bigBoy = multiplied.reduce((total,iteam,) => total + iteam);

document.getElementById('sumOfMultiplied').innerHTML = bigBoy;
