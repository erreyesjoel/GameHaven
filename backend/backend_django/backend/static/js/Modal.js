class Modal {
    // metodo para mostrar el modal de eliminar
    mostrarModalEliminar = (juegoId) => {
        const modalEliminar = document.querySelector('.modal-eliminar');
        // si le das a eliminar, se muestra el modal
        // esta none por defecto en css
        // pasa de none a block (none es oculto, block es visible)
        if (modalEliminar) {
            modalEliminar.style.display = 'block';
            modalEliminar.dataset.juegoId = juegoId; // guardamos el id del juego a eliminar

            // Manejar el clic en el botón de cancelar
            // cojo el boton de cancelar con el dom
            const btnCancelar = document.querySelector('.btn-cancelar-modal');
            // manejo el evento de click
            // pasa a ocultar el modal, si le damos a cancelar
            if (btnCancelar) {
                btnCancelar.onclick = () => {
                    modalEliminar.style.display = 'none';
                };
            }

            // Logica para que funcione eliminar juego del backend
            // Al hacer clic en "Eliminar", redirige a la vista eliminarJuego
            // boton en html con id confirmarEliminar
            const btnEliminar = document.querySelector('#confirmarEliminar');
            if (btnEliminar) {
                btnEliminar.onclick = () => {
                    window.location.href = `/juegos/eliminar/${juegoId}/`;
                };
            }
            // Manejar el clic fuera del contenido del modal para cerrarlo
            // si hacemos clic fuera del contenido del modal, se cierra
            window.onclick = (event) => {
                if (event.target === modalEliminar) {
                    modalEliminar.style.display = 'none';
                }
            };
        }
    }
}

// Esperar a que el DOM esté completamente cargado
document.addEventListener('DOMContentLoaded', () => {
    // Crear una instancia de la clase Modal
    const modal = new Modal();
    // Seleccionar todos los enlaces de eliminar
    const deleteLinks = document.querySelectorAll('.delete-link');

    // Mostrar el modal al hacer clic en cualquier icono de eliminar
    deleteLinks.forEach(link => {
        link.addEventListener('click', (e) => {
            e.preventDefault();
            // llamamos al método de la clase y le pasamos el id del juego
            modal.mostrarModalEliminar(link.dataset.id);
        });
    });
});