document.getElementById("login").addEventListener("submit", function(event) {
    var email = document.getElementById("exampleDropdownFormEmail1").value;
    var password = document.getElementById("exampleDropdownFormPassword1").value;
    
    if (!validateEmail(email)) {
      alert("Por favor, ingresa un correo electrónico válido.");
      event.preventDefault();
      return false;
    }
    
    if (!validatePassword(password)) {
      alert("La contraseña debe tener al menos 4 caracteres.");
      event.preventDefault();
      return false;
    }
    
    return true;
  });
  
  function validateEmail(email) {
    var re = /\S+@\S+\.\S+/;
    return re.test(email); 
  }
  
  function validatePassword(password) {
   
    return password.length >= 4;


  }

  const validarPassword = () => {
	const inputPassword = document.getElementById('password');
	

	if(inputPassword.value !== inputPassword.value){
		document.getElementById(`grupo__password`).classList.add('incorrecto');
		document.getElementById(`grupo__password`).classList.remove('correcto');
		document.querySelector(`#grupo__password i`).classList.add('fa-times-circle');
		document.querySelector(`#grupo__password i`).classList.remove('fa-check-circle');
		document.querySelector(`#grupo__password `).classList.add('error-activo');
		campos['password'] = false;
	} else {
		document.getElementById(`grupo__password`).classList.remove('grupo-incorrecto');
		document.getElementById(`grupo__password`).classList.add('grupo-correcto');
		document.querySelector(`#grupo__password i`).classList.remove('fa-times-circle');
		document.querySelector(`#grupo__password i`).classList.add('fa-check-circle');
		document.querySelector(`#grupo__password .input-error`).classList.remove('nput-error-activo');
		campos['password'] = true;
	}
}
  