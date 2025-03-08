var nombre="Julio"
var profesores= ["miguel", "pedro", "manolo", "marta", "petardo"]
var materias= ["ingles", "mti", "pendejo" ]

console.log(profesores.length)

document.write("<ul>");

profesores.forEach((element, indice) => {
    document.write("<li>" +indice+ " " +element + "</li>")
    
});
document.write("</ul>")