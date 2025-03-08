function consolita (n1,n2){
    console.log("La suma de dos numeros es ", n1+n2);
    console.log("La suma de dos numeros es ", n1-n2);
    console.log("La suma de dos numeros es ", n1*n2);
    console.log("La suma de dos numeros es ", n1/n2);
}

function pantallita (n1,n2){
    document.write("La suma de dos numeros es ", +n1+n2+"<br>");
    document.write("La suma de dos numeros es ", +n1-n2+"<br>");
    document.write("La suma de dos numeros es ", +n1*n2+"<br>");
    document.write("La suma de dos numeros es ", +n1/n2+"<br>");
}

function factos (n1, n2, mostrar=false){

    if(mostrar==false){
        consolita(n1,n2);
    }
    else{
        pantallita(n1,n2);
    } 
}
factos(15, 60, false)
factos(10, 70, true)