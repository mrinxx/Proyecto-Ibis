$(function(){
    $("#close").click(function(){
        document.getElementById("searchbar").style.display="none";
        document.getElementById("search").value=
        document.getElementById("content-news").innerHTML="";
        document.getElementById("content-events").innerHTML="";
        document.getElementById("content-resources").innerHTML="";
    })
    $("#search").keyup(function(){
        
        document.getElementById("content-news").innerHTML="";
        document.getElementById("content-events").innerHTML="";
        document.getElementById("content-resources").innerHTML="";
        let value=$(this).val();
        console.log(value.length)
        if(value!=""){
        $.ajax({
            url: '/search',
            method: 'GET',
            dataType: 'json',
            data:{
                'toSearch':value
            },
            success:function(data){
                
                const months=["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"];
                let dataEvents=JSON.parse(data.events).reverse();
                let dataNews=JSON.parse(data.news).reverse();
                let dataResources=JSON.parse(data.resources);
                
                dataNews.forEach(New => {
                    let newlink= document.createElement("a");
                    let linkparagraph=document.createElement("p");

                    newlink.textContent=New.fields.title;
                    newlink.href="news/details/"+New.pk;
                    linkparagraph.appendChild(newlink);
                    linkparagraph.className="found";
                    document.getElementById("content-news").appendChild(linkparagraph);
                    

                });

                dataResources.forEach(Resource => {
                    let description=document.createElement("p");
                    description.textContent=Resource.fields.description;
                    description.className="found";
                    document.getElementById("content-resources").appendChild(description);
                });

                dataEvents.forEach(Event => {
                    let eventparagraph=document.createElement("p");
                    let datespan=document.createElement("span");
                    let date=new Date(Event.fields.date);
                    datespan.textContent=date.getDate()+" de "+months[date.getMonth()]+" del "+date.getFullYear();
                    let description=document.createElement("span");
                    description.textContent=Event.fields.Description;
                    eventparagraph.textContent=datespan.textContent+" "+description.textContent;
                    eventparagraph.className="found";
                    document.getElementById("content-events").appendChild(eventparagraph);
                });


            },
            error:function(data){
                console.log("error")
                console.log(data)
            }
        })

    }})
})