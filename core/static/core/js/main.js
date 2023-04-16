let passsec = 0;


$(document).ready(function() {
    $("#basic-form").validate({
        rules: {
          name: {
            required: true },
          lastname:{
            required: true },
          age: {
            required: true,
            number: true,
            min: 18 },
          email: {
            required: true,
            email: true },
          password:{
            required: true,
            minlength: 6,
            maxlength: 18 },
          confirm_password:{
            required: true,
            equalTo: "#password" }
        },
        messages : {
          name: {
            minlength: "Name should be at least 3 characters" },
          age: {
            required: "Please enter your age",
            number: "Please enter your age as a numerical value",
            min: "You must be at least 18 years old" },
          email: {
            email: "El correo debe ser del formato: abc@dominio o abc@dominio.abc" },
          weight: {
            required: "People with age over 50 have to enter their weight",
            number: "Please enter your weight as a numerical value" }
        },
        submitHandler: function(form) {
            let edadcheck = document.getElementById("eBox").innerText;
            if (edadcheck == "1" && passsec == "1") form.submit();
            else if (passsec == "0") alert("La contraseña no cumple con los requisitos.");
            else alert("No puedes registrarte por ser menor de edad.");
          }});

    $(function(){
       var mayus = new RegExp("^(?=.*[A-Z])");
       var number = new RegExp("^(?=.*[0-9])");
       var lower = new RegExp("^(?=.*[a-z])");
       $("#password").on("keyup", function(){
            var pass = $("#password").val();
            if (mayus.test(pass) && number.test(pass) && lower.test(pass) ) {
              $("#mensaje").text("Segura");
              passsec = 1; }
            else {
               $("#mensaje").text("Insegura"); 
              passsec = 0; } }); 

    }); 

});
  

$(document).ready(function() {
    $("#sesionInicio").validate({
        rules: {
          email: {
            required: true,
            email: true }
        },
        messages : {
          email: {
            email: "Su nombre de usuario no tiene el formato de una dirección de correo.<br/>Debe tener el formato: abc@dominio o abc@dominio.abc" }
        }
        });

});

