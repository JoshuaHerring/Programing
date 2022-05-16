/* Lesson 4 */

/* DATA */

// Step 1: Declare a new variable to hold information about yourself

let me = 
{
    // Step 2: Inside of the object, add a property named name with a value of your name as a string
    name: 'Josh',

    // Step 3: Add another property named photo with a value of the image path and name (used in Task 2) as a string
    photo: 'images/me.jpg',

    // Step 4: Add another property named favoriteFoods with a value of an array of your favorite foods as strings ( hint: [] )
    favoriteFoods: ['Chicken', 'Pizza', 'Honey', 'Cereal', 'Sweets'],

    // Step 5: Add another property named hobbies with a value of an array of your hobbies as strings
    hobbies: ['Soccer', 'Hiking', 'Camping', 'Video Games', 'Kayaking'],
    
    
    
};

// Step 6: Add another property named placesLived with a value of an empty array
// Step 7: Inside of the empty array above, add a new object with two properties: place and length and values of an empty string
// Step 8: For each property, add appropriate values as strings
// Step 9: Add additional objects with the same properties for each place you've lived

me.placesLived = [
    {place:'Swan Valley', length:'2 Years'},
    {place: 'Stansbury Park', length: '18 Years'},
    {place: 'Mexico', length: '1 year'},
    {place: 'Rexburg', length:'1 year'}
]




/* OUTPUT */

// Step 1: Assign the value of the name property (of the object declared above) to the HTML <span> element with an ID of name
document.getElementById('name').innerHTML = me.name;

// Step 2: Assign the value of the photo property as the src attribute of the HTML <img> element with an ID of photo
document.getElementById('photo').src=me.photo;

// Step 3: Assign the value of the name property as the alt attribute of the HTML <img> element with an ID of photo
document.getElementById('photo').alt= me.name;

// Step 4: For each favorite food in the favoriteFoods property, create an HTML <li> element and place its value in the <li> element
me.favoriteFoods.forEach(food => {
    let fav_food_element = document.createElement('li');
    fav_food_element.innerHTML = food;

    // Step 5: Append the <li> elements created above as children of the HTML <ul> element with an ID of favorite-foods

    document.getElementById('favorite-foods').appendChild(fav_food_element);

})

// Step 6: Repeat Step 4 for each hobby in the hobbies property

me.hobbies.forEach(hobbie => {
    let hobbie_element = document.createElement('li');
    hobbie_element.innerHTML = hobbie;
    
    // Step 7: Repeat Step 5 using the HTML <ul> element with an ID of hobbies

    document.getElementById('hobbies').appendChild(hobbie_element);
})


// Step 8: For each object in the <em>placesLived</em> property:

me.placesLived.forEach(place => {
    // - Create an HTML <dt> element and put its place property in the <dt> element
    // - Create an HTML <dd> element and put its length property in the <dd> element
    let place_element = document.createElement('dt');
    place_element.innerHTML = place.place;
    let time_element = document.createElement('dd');
    time_element.innerHTML = place.length;

    // Step 9: Append the HTML <dt> and <dd> elements created above to the HTML <dl> element with an ID of places-lived
    document.getElementById('places-lived').appendChild(place_element);
    document.getElementById('places-lived').appendChild(time_element);
})


