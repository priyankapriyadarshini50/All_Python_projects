console.log("Connected")
var myOne = document.querySelector('#one')
var myTwo = document.querySelector("#two")
var myThree = document.querySelector("#three")

myOne.addEventListener("mouseover", function(){
    myOne.textContent = "Currently mouse is over me"
    myOne.style.color = 'red'
})

myOne.addEventListener('mouseout', function(){
    myOne.textContent = "HOVER OVER ME"
    myOne.style.color = 'black'
})

myTwo.addEventListener('click', function(){
    myTwo.textContent = 'Clicked on'
    myTwo.style.color = 'blue'
})

myThree.addEventListener('dblclick', function(){
    myThree.textContent = "Double clicked"
    myThree.style.color = 'orange'
})
