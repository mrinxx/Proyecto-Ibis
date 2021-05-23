$(document).ready(function(){
    //En esta petición se piden los tres primeros eventos que haya en la base de datos, en caso de que haya se crea el elemento
    //donde se visualiza y en caso contrario se muestra una alerta
    $.ajax({
        url: '/getfirstevents',
        method: 'GET',
        dataType: 'json',
        success: function (data){
            //json: Paso los eventos que se han recibido a un JSON para así manejarlos más facilmente
            // months: Lista que guarda los meses del año para compararlos con el que devuelve la fecha numéricamente
            const months=["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"];

            let jsonEvents=JSON.parse(data.events);
            if(jsonEvents.length==0){
                document.getElementById("see-more__events").style="display:none";
                createAlert("alertEvent");
            }else{
                for(element of jsonEvents){
                    let container=document.createElement("div");
                    container.className="event-container";
                    let date=new Date(element.fields.date);
                    
                    let containerdate=document.createElement("div");
                    containerdate.className="date";

                    let spanday=document.createElement("span");
                    spanday.className="date-day";
                    spanday.textContent=date.getDate();
                    let linebreak=document.createElement("br");

                    

                    let spanmonth=document.createElement("span");
                    spanmonth.className="date-month";
                    spanmonth.textContent=months[date.getMonth()];

                    containerdate.appendChild(spanday);
                    containerdate.appendChild(linebreak);
                    containerdate.appendChild(spanmonth);
                    container.appendChild(containerdate);

                    let containerdescription=document.createElement("div");
                    containerdescription.className="event";
                    let descriptiontext=document.createElement("p");
                    descriptiontext.textContent=element.fields.Description;

                    containerdescription.appendChild(descriptiontext);
                    container.appendChild(containerdescription);

                    document.getElementById("event-container").appendChild(container);
                }

            }

        },
        failure: function(data){
            console.log("failure");
            console.log(data);
        }
    });
    $.ajax({
        url: '/getfirstnews',
        method: 'GET',
        dataType: 'json',
        success: function (data){
            let jsonNews=JSON.parse(data.news).reverse();

            if(jsonNews.length==0){
                document.getElementById("see-more__news").style="display:none";
                createAlert("alertNews");
            }else{
                for(element of jsonNews){
                    let containernew=document.createElement("div");
                    
                    let containertitle=document.createElement("div");
                    containertitle.className="new-title";

                    let newtitle=document.createElement("h3");
                    newtitle.textContent=element.fields.title;
                    
                    containertitle.appendChild(newtitle);
                    containernew.appendChild(containertitle);
                    
                    let containerdescription=document.createElement("div");
                    containerdescription.className="new-description";

                    let containerdescriptiontext=document.createElement("div");
                    let text=document.createElement("p");
                    text.textContent=element.fields.subtitle;
                    text.className="new-description-text";
                    containerdescriptiontext.appendChild(text);

                    let principalimg=document.createElement("img");
                    principalimg.className="new-img";
                    //Aunque no es necesario, sin media/ no muestra la imagen
                    principalimg.src="/media/"+element.fields.media1;

                    containerdescription.appendChild(principalimg);
                    containerdescription.appendChild(containerdescriptiontext);

                    
                    containernew.appendChild(containerdescription);
                    document.getElementById("news-container").appendChild(containernew);
                }
             }

        },
        failure: function(data){
            console.log("failure");
            console.log(data);
        },
    });
});

function createAlert(divToShow){
    let notElementsWarn=document.getElementById(divToShow);
    notElementsWarn.style="display:block;border: 3px solid black;text-align: center;width: 85.5%;height:70px;margin: auto;border-radius: 10px;background-color: #FAA81D;font-weight: 800;margin-bottom:5%"
}