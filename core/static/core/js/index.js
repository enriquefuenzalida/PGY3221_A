
window.addEventListener("load", (event) => {
    if (localStorage.getItem("storageName") == "usuario") {
        document.getElementById("nav_admin").style.display = "none";
        document.getElementById("nav_registro").style.display = "none";
        document.getElementById("nav_inicio").style.display = "none";
        document.getElementById("nav_cerrar").style.display = "block";
        document.getElementById("nav_user").style.display = "block"; }
    else if (localStorage.getItem("storageName") == "admin") {
        document.getElementById("nav_admin").style.display = "block";
        document.getElementById("nav_registro").style.display = "none";
        document.getElementById("nav_inicio").style.display = "none";
        document.getElementById("nav_cerrar").style.display = "block";
        document.getElementById("nav_user").style.display = "none"; }
    else { 
    document.getElementById("nav_admin").style.display = "none";
    document.getElementById("nav_user").style.display = "none";
    document.getElementById("nav_registro").style.display = "block";
    document.getElementById("nav_inicio").style.display = "block";
    document.getElementById("nav_cerrar").style.display = "none"; }
  });

function cerrar(){
    var getInput = "null";
    localStorage.setItem("storageName",getInput); 
    window.location.href='index.html';
}
