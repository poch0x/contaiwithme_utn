(function() {
    // Función para actualizar el campo costo_total
    function actualizarCostoTotal() {
        var servicioField = document.getElementById('id_servicio');
        var costoTotalField = document.getElementById('id_costo_total');

        // Si el campo servicio está disponible y tiene valor
        if (servicioField && servicioField.value) {
            // Realizar una llamada AJAX al servidor para obtener el costo_base
            fetch(`/admin/servicios/servicio/${servicioField.value}/get_costo_base/`)
                .then(response => response.json())
                .then(data => {
                    // Actualizar el campo costo_total con el costo_base
                    if (data && data.costo_base) {
                        costoTotalField.value = data.costo_base;
                    }
                })
                .catch(error => console.error('Error al obtener el costo_base:', error));
        }
    }

    // Detectar cambios en el campo servicio
    var servicioField = document.getElementById('id_servicio');
    if (servicioField) {
        servicioField.addEventListener('change', actualizarCostoTotal);
    }

    // Llamar a la función al cargar la página en caso de que ya haya un servicio seleccionado
    window.addEventListener('load', actualizarCostoTotal);
})();
