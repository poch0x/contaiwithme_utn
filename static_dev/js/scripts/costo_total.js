// Archivo: static/admin/js/costo_total.js
function updateCostoTotal() {
    var servicioSelect = document.getElementById('id_servicio');
    var costoTotalInput = document.getElementById('id_costo_total');
    
    if (servicioSelect && costoTotalInput) {
        var selectedOption = servicioSelect.options[servicioSelect.selectedIndex];
        var costoBase = selectedOption.getAttribute('data-costo-base');
        
        if (costoBase) {
            costoTotalInput.value = costoBase;
        } else {
            costoTotalInput.value = '';
        }
    }
}

// Llamar a la función cuando la página se carga
document.addEventListener('DOMContentLoaded', function() {
    updateCostoTotal();
});