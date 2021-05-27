let agesmap= new Map();
agesmap.set("1E", '0-1 años');
agesmap.set("2E", '1-2 años');
agesmap.set("3E", '2-3 años');
agesmap.set("4E", '3-4 años');
agesmap.set("5E", '4-5 años');
agesmap.set("6E", '5-6 años');

let allTimetables;
let allMenus;

$(document).ready(function(){
    $.ajax({
        url:'/gettimetables',
        method:'GET',
        data:{},
        dataType: 'json',
        success: function (data){      
            let jsonTimetables=JSON.parse(data.timetables);
            allTimetables=jsonTimetables; //cargo en la lista todos los elementos que he recuperado
            if(jsonTimetables.length==0){
                document.getElementById("school-times__selector").style="display:none";
                document.getElementById("school-times__result").style="display:none";
                createAlert("alertTimetables");
            }else{
                for(timetable of jsonTimetables){
                    let selectdropdowntimetables=document.getElementById("school-times__selector");
                    let optionagetimetables=document.createElement("option");
                    optionagetimetables.value=agesmap.get(timetable.fields.age);
                    optionagetimetables.text=agesmap.get(timetable.fields.age)
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

    // $.ajax({
    //     url:'/getmenus',
    //     method:'GET',
    //     data:{},
    //     dataType: 'json',
    //     success: function (data){
    //         let selectdropdownmenus=document.getElementById("school-menus__selector");
    //         let jsonMenus=JSON.parse(data.menus);
    //         allMenus=jsonMenus; //cargo en la lista todos los elementos que he recuperado
    //         if(jsonMenus.length==0){
    //             document.getElementById("school-menus__selector").style="display:none";
    //             document.getElementById("school-menus__result").style="display:none";
    //             createAlert("alertMenus");
    //         }else{
    //         for(menus of jsonMenus){
    //             let optionagemenus=document.createElement("option");
    //             optionagemenus.value=agesmap.get(menus.fields.age);
    //             optionagemenus.text=agesmap.get(menus.fields.age)
    //             selectdropdownmenus.append(optionagemenus);
    //         }
    //     }
    //     },
    //     failure: function(data){
    //         console.log("failure");
    //         console.log(data);
    //     }
    // });
})


$(document).on('change','#school-times__selector',function(){
    var value = $(this).find("option:selected").attr("value");
    takeImage(allTimetables,"school-times__result","timetable",value)
});

$(document).on('change','#school-menus__selector',function(){
    var value = $(this).find("option:selected").attr("value");
    takeImage(allMenus,"school-menus__result","menu",value)    
});

function takeImage(elementsList,divTodisplay,type,value){
    document.getElementById(divTodisplay).innerHTML="";
    let selection;
    
    for(let key of agesmap){
        if(key[1]==value){
            selection=key[0];
        }
    }
    for(let element of elementsList){
        console.log(element);
        if(element.fields.age==selection){
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


