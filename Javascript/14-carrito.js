const  carrito = [
    {nombre: "Samsung LD 40 Pulgadas", precio: 500},
    {nombre: "Me Quede Sin Ideas", precio: 700},
    {nombre: "Onahole Turbo Sex 5000", precio: 200},
    {nombre: "Explosion Magistral", precio: 450},
    {nombre: "Samsung LD 40 Pulgadas", precio: 800},
    {nombre: "Audifonos JBL", precio: 150}   
]

const nuevoArray =carrito.map(function(producto){
    return `Articulo: ${producto.nombre} Precio: ${producto.precio *2}`
})

/*const nuevoArray2 =carrito.forEach(function(producto){
    console.log(`Articulo: ${producto.nombre} Precio: ${producto.precio}`)
})

console.log(nuevoArray)*/


for(let i =0; i<carrito.length; i++){
    console.log(`Articulo: ${carrito[i].nombre} Precio: $${carrito[i].precio}`)
}