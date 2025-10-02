class Login {
    // El constructor se ejecuta automáticamente al crear una instancia de la clase.
    // Sirve para inicializar atributos y preparar el objeto.
    constructor() {
        // Atributos de la clase (propiedades)
        /* atributo form
        atributo email
        atributo password 
        */
        this.form = document.querySelector('form');
        this.email = document.querySelector('#email');
        this.password = document.querySelector('#password');
        this.initEvents();
        this.initClearErrorOnInput(); // Limpia el error al escribir
    }
    
    // Limpia el mensaje de error cuando el usuario escribe en email o password
    initClearErrorOnInput = () => {
        const errorDiv = document.querySelector('.login-error');
        if (errorDiv) {
            [this.email, this.password].forEach(input => {
                input.addEventListener('input', () => {
                    errorDiv.remove();
                });
            });
        }
    }

    // Métodos de la clase
    initEvents = () => {
        if (this.form) {
            this.form.addEventListener('submit', (e) => this.validate(e));
        }
    }

    // metodo para validar el formulario
    validate = (e) => {
        // Validación simple de campos vacíos
        if (!this.email.value || !this.password.value) {
            e.preventDefault();
            this.showError('Por favor, rellena todos los campos.');
        }
    }

    // metodo para mostrar errores
    showError = (msg) => {
        let errorDiv = document.querySelector('.login-error');
        if (!errorDiv) {
            errorDiv = document.createElement('div');
            errorDiv.className = 'login-error';
            this.form.insertBefore(errorDiv, this.form.firstChild);
        }
        errorDiv.textContent = msg;
    }
}

// Inicializar la clase cuando cargue el DOM
document.addEventListener('DOMContentLoaded', () => new Login());