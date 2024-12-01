/**
 * Maneja el envío de formularios con SweetAlert para mostrar resultados.
 * @param {string} formId - El ID del formulario a procesar.
 * @param {string} successMessage - Mensaje a mostrar en caso de éxito.
 * @param {string} errorMessage - Mensaje a mostrar en caso de error.
 */
function handleFormSubmission(formId, successMessage, errorMessage) {
    const form = document.getElementById(formId);

    form.onsubmit = function (event) {
        event.preventDefault(); // Evita el envío estándar del formulario

        fetch(form.action, {
            method: form.method,
            body: new FormData(form)
        })
            .then(response => response.json())
            .then(data => {
                // Mostrar alerta de éxito con SweetAlert
                Swal.fire({
                    title: '¡Éxito!',
                    text: successMessage,
                    icon: 'success',
                    confirmButtonText: 'Aceptar'
                });
                form.reset(); // Limpiar el formulario
            })
            .catch(() => {
                // Mostrar alerta de error con SweetAlert
                Swal.fire({
                    title: 'Error',
                    text: errorMessage,
                    icon: 'error',
                    confirmButtonText: 'Aceptar'
                });
            });
    };
}

document.addEventListener("DOMContentLoaded", function () {
    // Verifica si los formularios existen antes de asignar eventos
    const asistenciaForm = document.getElementById("form-asistencia");
    const permisoForm = document.getElementById("form-permiso");

    if (asistenciaForm) {
        handleFormSubmission(
            "form-asistencia",
            "Asistencia registrada exitosamente.",
            "No se pudo registrar la asistencia. Inténtalo nuevamente."
        );
    }

    if (permisoForm) {
        handleFormSubmission(
            "form-permiso",
            "Permiso solicitado exitosamente.",
            "No se pudo enviar la solicitud de permiso. Inténtalo nuevamente."
        );
    }
});

