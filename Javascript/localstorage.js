'use strict'

if (typeof(Storage) !=='undefined') {
    console.log('Local Storage esta disponible')
} 
else {
    console.log('Local Storage no esta disponible')
    
}

localStorage.setItem("pendejos", "Yonaikel")

localStorage.getItem("pendejos")

console.log(localStorage.getItem("pendejos"))

document.querySelector("#curos").innerHTML=localStorage.getItem("pendejos")

var usuario={
    nombre: "Julio Infante",
    email: "julioelamantedetumadre8000@gmail.com",
    web: "mecorroaaaa.com"
}

localStorage.setItem("usuario",JSON.stringify(usuario))

//La forma correcta de almacenar datos en local storage es convirtiendo los objetos en JSONSTRING
//porque no puede procesar JAVASCRIPT puro, tambien debe convertirse en JSONSTRING al mandar una 
//informacion a un API

var userjs= JSON.parse(localStorage.getItem("usuario"))
console.log(userjs)

document.querySelector("#gafo").append(" " + userjs.nombre + userjs.web )