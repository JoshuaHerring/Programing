const begin1 = document.getElementById("begin1");
const button2 = document.getElementById("button2");
const button3 = document.getElementById("button3");
const button4 = document.getElementById("button4");
const button5 = document.getElementById("button5");
const button6 = document.getElementById("button6");
const button7 = document.getElementById("button7");
const button8 = document.getElementById("button8");
const button9 = document.getElementById("button9");
const button10 = document.getElementById("button10");
const button11 = document.getElementById("button11");
const button12 = document.getElementById("button12");
const story = document.getElementById("story");
const image = document.getElementById("backround_image")




function deactivate(button)
{
    button.classList.remove("active1");
    button.classList.remove("active2");
    button.classList.remove("active3");
    button.classList.add("inactive");
}

function activate1(button)
{
    button.classList.remove("inactive");
    button.classList.add("active1");
}

function activate2(button)
{
    button.classList.remove("inactive");
    button.classList.add("active2");
}

function activate3(button)
{
    button.classList.remove("inactive");
    button.classList.add("active3");
}


function begin1_event_handler()
{ 
    deactivate(begin1);
    story.innerHTML = "You enter the forest and you find a strange green creature sunbathing on a large rock.";
    image.src = "./images/lizard_rock.jpg";
    activate1(button2);
    activate2(button3);
    activate3(button4);
}

function button2_event_handler()
{
    story.innerHTML = "You snag him and and plop him on your shoulder to go on an adventure?"
    image.src ="./images/lizard_pet.jpg"
    deactivate(button2);
    deactivate(button3);
    deactivate(button4);
    activate1(button5);
    activate2(button6);
    activate3(button7);
}

function button3_event_handler()
{
    image.src = "./images/earthquake.jpg"
    story.innerHTML = "As you step on the little lizard you hear a thuderous crack as the ground begins to shake beneath you?"
    deactivate(button2);
    deactivate(button3);
    deactivate(button4);
    activate1(button8);
    activate2(button9);
    activate3(button10);
}

function button4_event_handler()
{
    image.src= "./images/cave.jpg"
    story.innerHTML = "You pull out a granola bar and point it at the little lizard. As you do the rock opens up and you fall in with the lizard."
    deactivate(button2);
    deactivate(button3);
    deactivate(button4);
    activate1(button11);
    activate2(button12);
}

function button5_eventhandler()
{
    image.src = "./images/boulder.jpg"
    story.innerHTML = "You take off with your new pet lizard and after a moment of running all goes black as a massive boulder crashes on top of you."
    deactivate(button5);
    deactivate(button6);
    deactivate(button7);
}

function button6_eventhandler()
{
    deactivate(button5);
    deactivate(button6);
    deactivate(button7);
}

function button7_eventhandler()
{
    deactivate(button5);
    deactivate(button6);
    deactivate(button7);
}

function button8_eventhandler()
{
    deactivate(button8);
    deactivate(button9);
    deactivate(button10);
}

function button9_eventhandler()
{
    deactivate(button8);
    deactivate(button9);
    deactivate(button10);
}

function button10_eventhandler()
{
    deactivate(button8);
    deactivate(button9);
    deactivate(button10);
}

function button11_eventhandler()
{
    deactivate(button11);
    deactivate(button12);
}

function button12_eventhandler()
{
    deactivate(button11);
    deactivate(button12);
}


begin1.addEventListener("click", begin1_event_handler);
button2.addEventListener("click", button2_event_handler);
button3.addEventListener("click", button3_event_handler);
button4.addEventListener("click", button4_event_handler);
button6.addEventListener("click", button6_eventhandler);
button7.addEventListener("click", button7_eventhandler);
button8.addEventListener("click", button8_eventhandler);
button9.addEventListener("click", button9_eventhandler);
button5.addEventListener("click", button5_eventhandler);
button10.addEventListener("click", button10_eventhandler);
button11.addEventListener("click", button11_eventhandler);
button12.addEventListener("click", button12_eventhandler);