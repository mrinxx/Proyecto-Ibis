

let allTimetables;
let allMenus;
let allCiclesTimetables;

$(document).ready(function(){
    $.ajax({
        url:'/gettimetables',
        method:'GET',
        data:{},
        dataType: 'json',
        success: function (data){      
            let jsonTimetables=JSON.parse(data.timetables);
            allTimetables=jsonTimetables; //cargo en la lista todos los elementos que he recuperado
            let jsonCicles=JSON.parse(data.cicles);
            allCiclesTimetables=jsonCicles;

            if(jsonTimetables.length==0){
                document.getElementById("school-times__selector").style="display:none";
                document.getElementById("school-times__result").style="display:none";
                createAlert("alertTimetables");
            }else{
                for(let cicle of jsonCicles){
                    let selectdropdowntimetables=document.getElementById("school-times__selector");
                    let optionagetimetables=document.createElement("option");
                    optionagetimetables.value=cicle.fields.classroom
                    optionagetimetables.text=cicle.fields.classroom;
                    selectdropdowntimetables.append(optionagetimetables);
                }
        }
        },
        failure: function(data){
            console.log("failure");
            console.log(data);
        }
    });
    $.ajax({
        url:'/getmenus',
        method:'GET',
        data:{},
        dataType: 'json',
        success: function (data){
            let selectdropdownmenus=document.getElementById("school-menus__selector");
            let jsonMenus=JSON.parse(data.menus);
            allMenus=jsonMenus; //cargo en la lista todos los elementos que he recuperado
            if(jsonMenus.length==0){
                document.getElementById("school-menus__selector").style="display:none";
                document.getElementById("school-menus__result").style="display:none";
                createAlert("alertMenus");
            }else{
            for(menus of jsonMenus){
                let optionagemenus=document.createElement("option");
                optionagemenus.value=agesmap.get(menus.fields.age);
                optionagemenus.text=agesmap.get(menus.fields.age)
                selectdropdownmenus.append(optionagemenus);
            }
        }
        },
        failure: function(data){
            console.log("failure");
            console.log(data);
        }
    });

    
})


$(document).on('change','#school-times__selector',function(){
    var value = $(this).find("option:selected").attr("value");
    takeImage(allTimetables,allCiclesTimetables,"school-times__result","timetable",value)
});

$(document).on('change','#school-menus__selector',function(){
    var value = $(this).find("option:selected").attr("value");
    takeImage(allMenus,allCiclesMenus,"school-menus__result","menu",value)    
});

function takeImage(elementsList,cicles,divTodisplay,type,value){
    document.getElementById(divTodisplay).innerHTML="";
    let selection;

    for(let cicle of cicles){
        if(value==cicle.classroom){
            selection=cicle.pk;
        }
    }

    for(let element of elementsList){
        if(element.fields.cicle_id==selection){
            let resultimage=document.createElement("img");
            let imageTodisplay;
            if(type=="timetable"){
                imageTodisplay="/media/"+element.fields.timetable_image;
            }else if(type=="menu"){
                imageTodisplay="/media/"+element.fields.menu_image;
            }
            resultimage.src=imageTodisplay;
            document.getElementById(divTodisplay).appendChild(resultimage);
        }
    }
}

function createAlert(divToShow){
    let notElementsWarn=document.getElementById(divToShow);
    notElementsWarn.style="display:block;border: 3px solid black;text-align: center;width: 85.5%;height:70px;margin: auto;border-radius: 10px;background-color: #FAA81D;font-weight: 800;margin-bottom:5%"
}


