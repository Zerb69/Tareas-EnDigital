function listadofrutas(fruta1, fruta2,...todasFrutas){
    console.log("La primera fruta es:" +fruta1)
    console.log("La segundo fruta es:" +fruta2)
    console.log(todasFrutas)
}
listadofrutas("Melocoton", "Fresa", "Fresa (cuca)", "Naranja", "Pera")
var frutas2=["ano", "ano2", "ano3", "ano4", "ano5"];

listadofrutas(...frutas2)