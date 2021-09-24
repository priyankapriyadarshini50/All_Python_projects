console.log('connected')

var restart = document.querySelector('#two')

var box = document.querySelectorAll('td');


restart.addEventListener('click', function(){
    for(var i=0; i<box.length;i++){
        box[i].textContent= ' ';
    }
})

for(var i=0; i < box.length; i++){
    box[i].addEventListener('click', function(){
        if(this.textContent === ' '){
            this.textContent='X';
        }else if(this.textContent === 'X'){
            this.textContent = 'O';
        }else{
            this.textContent = ' ';
        }
        })

}
