
/* -revealpass: recibe el id del botón que permite ver la contraseña, cambia el tipo del campo a texto para que este sea visible
    e indica que si se vuelve a hacer click sobre el botón, se vuelva a esconder la contraseña.
   -hidepass: Hace lo mismo que la anterior pero para esconder la contraseña*/

function revealpass(idfield){
    document.getElementById("password").type="text";
    document.getElementById(idfield).onclick=function(){hidepass(idfield)};
}

function hidepass(idfield){
    document.getElementById("password").type="password";
    document.getElementById(idfield).onclick=function(){revealpass(idfield)};
}