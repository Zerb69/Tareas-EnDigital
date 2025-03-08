/*function sumar(a, b){
    return a+b
}

const resultado = sumar(20,30)
console.log(resultado)*/


/*let total=0
function agregarCarrito(precio){
    return total+=precio
}

function calcularImpuesto(total){
    return 1.15*total
}

total=agregarCarrito(200)
total=agregarCarrito(300)
total=agregarCarrito(400)
console.log(total)*/

/*const reproductor ={
    reproducir: id=> console.log(`Reproduciendo cancion id ${id}`),
    pausar: id=> console.log(`Pausando la cancion id ${id}...`),
    borrar: id=> console.log(`Borrando la cancion id: ${id}`),
    crearPlaylist: id=> console.log(`Creando la Playlist ${nombre}`),
    reproducirPlaylist: id=> console.log(`Reproduciendo la Playlist ${nombre}`)
}

set nuevaCancion(cancion){
    this.cancion=cancion
    console.log(`Añadiendo ${this.cancion}`)*/



const vroomvroom ={
    modelo: '',
    encender: (modelo) =>console.log(`Me estas prendiendo, y tambien el ${modelo}`),
    apagar: (modelo) =>console.log(`Puta madre me apagaste el hue- digo el ${modelo}`),
    retroceder: (modelo) =>console.log(`No tengo ningun chiste para esto en español, retrocediendo el ${modelo}`),

    set nuevoCarro(modelo){
        this.modelo=modelo
        console.log(`Fijando ${this.modelo}`)
    },

    get obtenerCarro(){
        console.log(`${this.modelo}`)
    }
}
vroomvroom.nuevoCarro="Toyota"
vroomvroom.obtenerCancion

vroomvroom.encender(vroomvroom.modelo),
vroomvroom.apagar(vroomvroom.modelo),
vroomvroom.retroceder(vroomvroom.modelo)

console.log(Object.keys(vroomvroom))
console.log(Object.values(vroomvroom))
console.log(Object.entries(vroomvroom))