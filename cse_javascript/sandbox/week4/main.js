// fetch

setTimeout(function(){
    console.log('first enterd second to appear');
}, 1000)

console.log('second entered first to appear');

const url = 'the url of the website you want the data from.'


async function learn_fetch(url){
    
    // gets json file from web address
    const response = await fetch(url);

    if (response.ok){
// changing the json file to javascript
        const data = await response.json();
        // use it in a function now
        dostuff(data);
}
}
