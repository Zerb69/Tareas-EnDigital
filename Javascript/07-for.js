// const ciudad = ["San Juan", "Maracay", "Tucupido", "Merida", "Petare", "Delta Amacuro"]

// for (let i=0; i<ciudad.length; i++) {
//     console.log(ciudad[i]) + "<br>";

// }


const numero = [10, 20, 30, 40, 50];
let text="";
for (let i=0; i<numero.length; i++) {
    text += numero[i] + "<br>";
}

document.getElementById("numero").innerHTML = text;