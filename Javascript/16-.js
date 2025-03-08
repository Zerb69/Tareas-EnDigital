/*console.log(1)
    document.addEventListener('DOMContentLoaded', () => {
        console.log(2);
    })
console.log(3);*/

const nav = document.querySelector('.navbar')

nav.addEventListener('mousedown', () => {
    console.log('Entrando a navegar')

    nav.style.backgroundColor = 'purple'
})

nav.addEventListener('dblclick',() => {
    console.log('saliendo de la navegacion')

    nav.style.backgroundColor = 'yellow'
})

const calcu ={
    sumar: function(n1,n2){
        suma=n1+n2
        document.getElementById("resulta").innerHTML =`La suma de a: ${n1} mas ${n2}=${suma}`
    },
    restar: function(n1,n2){
        resta=n1-n2
        document.getElementById("resulta").innerHTML =`La resta de a: ${n1} menos ${n2}=${resta}`
    },
    multiplicar: function(n1,n2){
        multi=n1*n2
        document.getElementById("resulta").innerHTML =`La multiplicacion de a: ${n1} por ${n2}=${multi}`
    },
    dividir: function(n1,n2){
        divi=n1/n2
        document.getElementById("resulta").innerHTML =`La division de a: ${n1} entre ${n2}=${divi}`
    },
}

const tablita = {
    nombres: function(){
        var gente =["Pedro", "Miguel", "Marco", "Huevon", "Pendejo", "Calamardo", "Mephistoteles"]
    }
}