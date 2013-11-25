function textCounter(field, countfield, maxlimit) {
	if (field.value.length > maxlimit)
		field.value = field.value.substring(0, maxlimit);
	else 
		countfield.value = maxlimit - field.value.length;
}

function textCounterSec(field,maxlimit){
	if (field.value.length > maxlimit) 
		field.value = field.value.substring(0,maxlimit);
	}

function validar() {
	var estaTodoOK = true;
	if (document.getElementById("secuencia1").value>4 || document.getElementById("secuencia1").value<1 ||  isNaN(document.getElementById("secuencia1").value)) {
		estaTodoOK = false;	
	}	

	if (document.getElementById("secuencia2").value>4 || document.getElementById("secuencia2").value<1 || isNaN(document.getElementById("secuencia2").value)) {
		estaTodoOK = false;	
	}

	if (document.getElementById("secuencia3").value>4 || document.getElementById("secuencia3").value<1 || isNaN(document.getElementById("secuencia3").value)) {
		estaTodoOK = false;	
	}

	if (document.getElementById("secuencia4").value>4 || document.getElementById("secuencia4").value<1 || isNaN(document.getElementById("secuencia4").value)) {
		estaTodoOK = false;	
	}

	var sec1 = document.getElementById("secuencia1").value;
	var sec2 = document.getElementById("secuencia2").value;
	var sec3 = document.getElementById("secuencia3").value;
	var sec4 = document.getElementById("secuencia4").value;

	if (sec1 == sec2 || sec1 == sec3 || sec1 == sec4 || sec2 == sec3 || sec2 == sec4 || sec3 == sec4){
		estaTodoOK = false;
	}

	if (!estaTodoOK) {
		alert("Los numeros de secuencia: \n  * deben ser entre 1 y 4 \n  * no pueden ser letras \n  * no pueden estar repetidos!");	
	}

	return estaTodoOK;
}

function valid_register(){
	var estaTodoOK = true;
	if(document.getElementById("password1").value.length < 6 || document.getElementById("password2").value.length < 6){
		estaTodoOK = false;
	}

	if(!estaTodoOK){
		alert("la contraseña debe ser mayor a 6");
	}

	return estaTodoOK;
}