//En este documento se ve como facilita el uso de django la muestra de elementos por pantalla
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
            //en caso de que no haya eventos se va mostrar un mensaje
            if(jsonEvents.length==0){
                document.getElementById("see-more__events").style="display:none";
                createAlert("alertEvent");
            }else{
                //En caso de que haya eventos:
                //Para cada elemento se va a crear el contenedor donde se muestran todos los datos y se va a hacer que 
                //se muestre en pantalla
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
                    spanmonth.textContent=months[date.getMonth()]; //se coge el mes que corresponde en la lista de meses declarada

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
});

//muestra la alerta cuando no hay ningún elemento, eventos en este caso
function createAlert(divToShow){
    let notElementsWarn=document.getElementById(divToShow);
    notElementsWarn.style.display="block";
}