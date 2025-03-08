var n1= parseInt(prompt("Introduce el primer numero", 0));
var n2= parseInt(prompt("Introduce el segundo numero", 0));

if (n1>n2){
   console.log("El primer numero " +n1+ " es mayor y el segundo numero " +n2+ " es menor")
}

else if (n1==n2){
    console.log("Ambos numeros " +n1+ " y " +n2+ " son iguales")
}

else{
    console.log("El segundo numero " +n2+ " es mayor y el primer numero " +n1+ " es mayor")
}

console.log(n1, n2)
