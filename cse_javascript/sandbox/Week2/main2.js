// comparisons

console.log(5 > 9);
console.log('5' == 5 && 6 == 6);

// conditionals

let your_age = 19;

if (your_age >= 18)
{
    console.log('Votable');
}
else
{
    console.log('not votable');
};
let num_sales = 100000;

if (num_sales <= 50)
{
    console.log('Way few to sales');
}
    else if (num_sales <= 1000)
    {
        console.log('average sales');
    }
    else
    {
       console.log('good sales');
    }


let grade = 'a';
let gpa = 0;

switch(grade)
{
    case 'a':
        gpa = 4;
        break;
    case 'b':
        gpa = 3;
        break;
    case 'c':
        gpa = 2;
        break;
    default:
        gpa = 0;
}
console.log(gpa)

// functions

let number = Math.random();
console.log(number);

function flip()
{
    if (number < .5)
    {
        console.log('Heads');
    }
        else
        {
            console.log('tails');
        }
}
flip()