'use strict'

var formulario = document.querySelector('#formulario')
var ul = document.querySelector('#listarjuegos')

function construirLista(){
    ul.innerHTML=''
    for (var i in localStorage){
        if (typeof localStorage[i] === 'string') {
            var li =document.createElement('li')
            li.textContent = localStorage[i]
            ul.appendChild(li)
        }
    }
}

construirLista()

formulario.addEventListener('submit', function(event) {
    event.preventDefault()

    var juego = document.querySelector('#addjuego').value
    if(juego.length >=1) {
        localStorage.setItem(juego, juego)
        construirLista()
    }
})