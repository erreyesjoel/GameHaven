class Modal {
    // metodo para mostrar el modal de eliminar
    // ahora es reutilizable para cualquier tipo (juegos, plataformas, etc.)
    mostrarModalEliminar = (id, tipo) => {
        const modalEliminar = document.querySelector('.modal-eliminar');
        // si le das a eliminar, se muestra el modal
        // esta none por defecto en css
        // pasa de none a block (none es oculto, block es visible)
        if (modalEliminar) {
            modalEliminar.style.display = 'block'; // muestra el modal
            modalEliminar.dataset.id = id; // guarda el id del elemento
            modalEliminar.dataset.tipo = tipo; // guarda el tipo del elemento

            // Personalizar el texto según el tipo
            const textoModal = modalEliminar.querySelector('.texto-modal');
            const tituloModal = modalEliminar.querySelector('.h2-modal-eliminar');
            const btnConfirmar = modalEliminar.querySelector('#confirmarEliminar');

            if (tipo === 'usuarios') {
                tituloModal.textContent = 'Confirmar baja';
                textoModal.textContent = '¿Estás seguro de que deseas dar de baja a este usuario?';
                btnConfirmar.textContent = 'Dar de baja';
            } else {
                tituloModal.textContent = 'Confirmar eliminación';
                textoModal.textContent = '¿Estás seguro de que deseas eliminar este elemento?';
                btnConfirmar.textContent = 'Eliminar';
            }

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

            // Logica para que funcione eliminar del backend
            // Al hacer clic en "Eliminar", redirige a la vista correspondiente
            // boton en html con id confirmarEliminar
            const btnEliminar = document.querySelector('#confirmarEliminar');
            if (btnEliminar) {
                btnEliminar.onclick = () => {
                    window.location.href = `/${tipo}/eliminar/${id}/`;
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
            // llamamos al método de la clase y le pasamos el id y el tipo
            // tipo: 'juegos', 'plataformas', etc. (debe estar en data-tipo en el HTML)
            const tipo = link.dataset.tipo;
            modal.mostrarModalEliminar(link.dataset.id, tipo);
        });
    });
});