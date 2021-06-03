
function search(){
    document.getElementById("searchbar").style.display="block";
}
$(function(){ 
$("#close").click(function(){
    document.getElementById("searchbar").style.display="none";
})
})

function darkMode(){
    let headericon=document.getElementById("dark-icon");
    headericon.className='far fa-sun';
    headericon.onclick = function() {lightMode()};
    let headers1=document.getElementsByTagName("h1");
    for(headers of headers1){
        headers.style="color:#F9F9F8";
    }

    let headers2=document.getElementsByTagName("h2");
    for(headers of headers2){
        headers.style="color:#F9F9F8";
    }

    let listlinks=document.getElementsByTagName("a");
    for(item of listlinks){
        item.style="color:#F9F9F8"
    }


    let listmybuttons=document.getElementsByClassName("see-more");
    for(item of listmybuttons){
        item.style="color:black"
    }

    document.getElementById('');
    for(item of listmybuttons){
        item.style="color:black"
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
    let headericon=document.getElementById("dark-icon");
    headericon.className='far fa-moon';
    headericon.onclick='test()';

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

function displayMenu(){
    let menu=document.getElementById('min_menu');
    if(menu.style.display=="none"){
        menu.style.display="block";
    }else{
        menu.style.display="none";
    }
}