const myArray = [12, 34, 21, 54];

const lucky_number = 21;

let lucky_index = myArray.indexOf(lucky_number);

console.log(lucky_index);


// map array method - copys the original array into a new variable you have set without changing the original
array1 = [1, 2, 4, 7, 9];

const map1 = array1.map(x => x * 2);

console.log(array1);
console.log(map1);

// reduce, reduces all iteams in an array down to 1 number

const gpa_points = [3, 4, 3, 2, 1];

const point_total = gpa_points.reduce(function(total, item)
{
    return total + item;
})
const gpa = point_total / gpa_points.length;

console.log(gpa);

// you can easily make this code simpler you know how
// theese are just the teachers unsimplified examples


// filter, will filter based on a condition and makes a new array

const words = ['water', 'earth', 'fire', 'air', 'darkness', 'unholy'];

// uses arrow function, to the left of the arrow is your variable input to the right is your logic and output
const shortwords = words.filter((word) => word.length <5);


console.log(words);
console.log(shortwords);