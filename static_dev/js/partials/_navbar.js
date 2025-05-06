// Selecciona todos los enlaces dentro de la lista de navegación
const enlaces = document.querySelectorAll('.navbar-nav .nav-link');

// Función para agregar la clase al pasar el cursor
function agregarClaseVerde(event) {
    event.target.classList.add('nav-link-hover');
}

// Función para quitar la clase al quitar el cursor
function quitarClaseVerde(event) {
    event.target.classList.remove('nav-link-hover');
}

// Agrega los event listeners a cada enlace
enlaces.forEach(enlace => {
    enlace.addEventListener('mouseover', agregarClaseVerde);
    enlace.addEventListener('mouseout', quitarClaseVerde);
});