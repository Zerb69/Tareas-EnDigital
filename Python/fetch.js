var div_usuarios = document.querySelector("#usuarios")
fetch('https://reqres.in/api/users')
    .then(data => data.json())

    .then(personas =>{
        usuarios = personas.data
        console.log(usuarios)

        usuarios.map((personas, i) =>{
            let nombre = document.createElement('h3')
            nombre.innerHTML = i + " - " + personas.first_name + " " + personas.last_name

            div_usuarios.append(nombre)
        })
    })

    .catch(error => console.error('Error al obterner datos:', error));