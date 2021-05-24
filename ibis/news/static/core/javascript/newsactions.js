// //Esta variable almacenará todas las noticias que se rescaten de la base de datos para poder manejarlas y cargar las anteriores o las posteriores
let newslist; 
// //contador de las noticias totales que se están mostrando
let newsdisplayed=0;

 $(document).ready(function(){
     /*Se hace una petición al servidor para rescatar todas las noticias:
         -Si NO hay noticias -> Se informa de ello
         -Si hay más de 6 noticias -> Se cogen las primeras
         -Si hay entre 1 y 5 noticias -> Se cogen TODAS */
     $.ajax({
         url:'/news/getnews',
         method: 'GET',
         dataType: 'json',
         success: function (data){
             //Paso de lo recibido a JSON para facilitar el manejo
             //Se le da la vuelta para que aparezcan los más recientes primeros
             let jsonNews=JSON.parse(data.news).reverse(); 
             newslist=jsonNews;  //Se cargan los datos en la lista
            
             if(jsonNews.length==0){
                 document.getElementById("charge-news").style="display:none";
                 createAlert("alert");
             }else{
                let newscounter=0; //contador de noticias que se han procesado
                 if(jsonNews.length>6){
                     while(true){
                         let actualnew=jsonNews[newscounter];
                         createView(actualnew);
                         newscounter++; //se pasa a la siguiente noticia aumentando el contador
                         newsdisplayed++; //se suma una noticia al total de las mostradas en la web
                         //Cuando se hayan procesado 6 noticias se para
                         if(newscounter==6){
                            break;
                         }
                    }
                }  
                else if(jsonNews.length>=1 && jsonNews.length<=6){
                    document.getElementById("charge-news").style="display:none";
                    for(element of jsonNews){
                        createView(element);
                    }
                }     
         }
     },
         failure:function(data){
             console.log("failure");
             console.log(data);
         }
     });
})

/*Esta función toma la lista en la que se han cargado todas las noticias y el contador de todas las noticias
que se están mostrando en la página.
Se comienza procesando la noticia que ocupa el lugar en el que se han dejado de procesar las anteriores
Se suma uno a las noticias mostradas y cuando hay 6 más, se termina */

function charge(){
    console.log(newsdisplayed);
    let auxcont=newsdisplayed;
    if(newslist.length-newsdisplayed>6){
        while(true){
            createView(newslist[newsdisplayed]);
            newsdisplayed++;
            if(newsdisplayed==auxcont+6){
                break
            }
        }
    }
    else if(newslist.length-newsdisplayed<=6){
        for(let i=newsdisplayed;i<=newslist.length;i++){
            createView(newslist[i]);
        }
    }
    // while(true){
    //     createView(newslist[newsdisplayed]);
    //     newsdisplayed++;
    //     if(newsdisplayed==auxcont+6){
    //         break;
    //     }
    // }
}

//Con esta función se muestra que no hay noticias en caso de que no haya noticias
function createAlert(divToShow){
     let notElementsWarn=document.getElementById(divToShow)
     notElementsWarn.style="display:block;border: 3px solid black;text-align: center;width: 85.5%;height:70px;margin: auto;border-radius: 10px;background-color: #FAA81D;font-weight: 800;margin-bottom:5%";
}

function createView(element){
    let containernew=document.createElement("div");
    containernew.id=element.fields.title;

    
    let containertitle=document.createElement("div");
        containertitle.className="new-title";

        let newtitle=document.createElement("h3");
        newtitle.textContent=element.fields.title;
                    
        containertitle.appendChild(newtitle);
        containernew.appendChild(containertitle);
                    
        let containerdescription=document.createElement("div");
        containerdescription.className="new-description";
        containerdescription.id=element.fields.title;
        // containerdescription.onclick="test()";

        let containerdescriptiontext=document.createElement("div");
        let text=document.createElement("a");
        text.href="details/"+element.pk;
        text.textContent=element.fields.subtitle;
        text.className="new-description-text";
        containerdescriptiontext.appendChild(text);

        let principalimg=document.createElement("img");
        principalimg.className="new-img";
        principalimg.src="/media/"+element.fields.media1;

        containerdescription.appendChild(principalimg);
        containerdescription.appendChild(containerdescriptiontext);

                    
        containernew.appendChild(containerdescription);
        document.getElementById("news-container").appendChild(containernew);
}


// $(document).on("click",".new-description", function () {
//     // var clickedBtnID = $(this).attr('id'); // or var clickedBtnID = this.id
//     // alert('you clicked on button #' + clickedBtnID);
//         // Generate URL without "id" bit
//         var url = "{% url 'details' %}";
    
//         var id = $(this).attr('id');
    
//         // Construct the full URL with "id"
//         document.location.href = "details/"+id;
// });
 