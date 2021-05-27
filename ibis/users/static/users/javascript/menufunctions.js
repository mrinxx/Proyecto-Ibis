
function search(){
    alert("implement search bar !!!!!");
}


function darkMode(){
    document.getElementById("dark-icon").style="display:none";
    document.getElementById("light-icon").style="display:inline-block";
    document.getElementById("min-dark-icon").style="display:none";
    document.getElementById("min-light-icon").style="display:inline-block";

    let headers1=document.getElementsByTagName("h1");
    for(headers of headers1){
        headers.style="color:#F9F9F8";
    }

    let headers2=document.getElementsByTagName("h2");
    for(headers of headers2){
        headers.style="color:#F9F9F8";
    }

    let listitems=document.getElementsByTagName("li");
    for(item of listitems){
        item.style="color:#F9F9F8"
    }

    document.getElementById("zona-logo").style="background-color:#333533";
    document.body.style.backgroundColor="#333533";
    document.getElementById("max-menu-navegacion").style="background-color:#202020;color:#F9F9F8";
    document.querySelector('footer').style ="background-color:#202020;color:#F9F9F8";
    document.getElementById('footer-max_social-media').style="color:black";
    let eventsdisplay=document.getElementsByClassName('event');
    for(part of eventsdisplay){
        part.style="background-color:#202020;color:#F9F9F8";
    }

}
function lightMode(){
    document.getElementById("light-icon").style="display:none";
    document.getElementById("dark-icon").style="display:inline-block";
    document.getElementById("zona-logo").style="background-color:#FAA81D";
    document.getElementById("max-menu-navegacion").style="background-color:#FFC267";
    document.querySelector('footer').style ="background-color:##FAA81D;color:black";
    let eventsdisplay=document.getElementsByClassName('event');
    for(part of eventsdisplay){
        part.style="background-color:#F9F9F8;color:black";
    }
    document.body.style="background-color:#F9F9F8";
    location.reload(); //lo hago ya que se producen errores al cambair el tamaño de pantalla
    
}

function lightModeMobile(){
    document.getElementById("min-light-icon").style="display:none";
    document.getElementById("min-dark-icon").style="display:inline-block";
    document.getElementById("zona-logo").style="background-color:#F9F9F8";

    document.querySelector('footer').style ="background-color:##FAA81D;color:black";
    let eventsdisplay=document.getElementsByClassName('event');
    for(part of eventsdisplay){
        part.style="background-color:#F9F9F8;color:black";
    }
    document.body.style="background-color:#F9F9F8";
    location.reload();
}

function displayMenu(){
    let menu=document.getElementById('min_menu');
    if(menu.style.display=="none"){
        menu.style.display="block";
    }else{
        menu.style.display="none";
    }
}