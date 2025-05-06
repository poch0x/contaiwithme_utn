$(document).ready(function () {

    // boton saludar con id=saludito
    $('#saludito').on('click', function (event) {
        event.preventDefault();
        alert("Hola desde configuracion");
    });

});
