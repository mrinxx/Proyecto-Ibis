function Guardian(codigo,username,password,dni,nombre,apellidos,nacimiento,tipovia,nombrevia,numerovia,piso,letra,cp,ciudad,email,numero,acuerdoprivacidad,terminos,newsletter,activado,imagen){
    this.codigo=codigo;
    this.username=username;
    this.password=password;
    this.dni=dni;
    this.nombre=nombre;
    this.apellidos=apellidos;
    this.nacimiento=nacimiento;
    this.tipovia=tipovia,
    this.nombrevia=nombrevia,
    this.numerovia=numerovia,
    this.piso=piso,
    this.letra=letra,
    this.cp=cp,
    this.ciudad=ciudad,
    this.email=email;
    this.numero=numero;
    this.acuerdoprivacidad=acuerdoprivacidad;
    this.terminos=terminos;
    this.newsletter=newsletter;
    this.activado=activado;
    this.imagen=imagen;
}

let allinputs=document.getElementsByTagName('input');
let allselects=document.getElementsByTagName('select');
let elementicon=document.getElementById("icon");
let elementbutton=document.getElementById("edit-personal-data");

$(function(){ 
    $("#passwordchanger").click(function(){
        $("#passwordModal").show();
    })

    $("#close-modal").click(function(){
        $("#passwordModal").hide();
    })

    for(input of allinputs){
        input.disabled=true;
    }

    
    for(select of allselects){
        select.disabled=true;
    }

    

    $.ajax({
        url:'/users/guardiandetails',
        method:"GET",
        data:{},
        dataType:'json',
        success:function(data){            
            let jsonGuardian=JSON.parse(data.guardian); //guarda los datos especificos de la tabla guardian
            let jsonUser=JSON.parse(data.user); //guarda los datos especificos de la tabla user
              
            //establezco guardian de tipo Guardian para poder acceder más facilmente a los datos que debe de
            //tener el tutor de los alumnos
                guardian=new Guardian(
                    jsonGuardian[0].pk,
                    jsonUser[0].fields.username,
                    jsonUser[0].fields.password,
                    jsonGuardian[0].fields.dni,
                    jsonUser[0].fields.first_name,
                    jsonUser[0].fields.last_name,
                    jsonGuardian[0].fields.birth_date,
                    jsonGuardian[0].fields.via_type,
                    jsonGuardian[0].fields.via_name,
                    jsonGuardian[0].fields.via_number,
                    jsonGuardian[0].fields.address_floor,
                    jsonGuardian[0].fields.floor_letter,
                    jsonGuardian[0].fields.cp,
                    jsonGuardian[0].fields.city,
                    jsonUser[0].fields.email,
                    jsonGuardian[0].fields.phone,
                    jsonGuardian[0].fields.privacity,
                    jsonGuardian[0].fields.terms,
                    jsonGuardian[0].fields.newsletter,
                    jsonGuardian[0].fields.activated,
                    jsonGuardian[0].fields.image
                    );

                    
                    
                        // document.getElementById('id_dni').value=guardian.dni.toUpperCase();
                        // document.getElementById('name').value=guardian.nombre;
                        // document.getElementById('username').value=guardian.username;
                        // document.getElementById('last_name').value=guardian.apellidos;
                        document.getElementById('id_birthdate').value=guardian.nacimiento;
                        document.getElementById("id_viatype").selected=guardian.viatipo;
                        document.getElementById("id_vianame").value=guardian.nombrevia;
                        document.getElementById("id_vianumber").value=guardian.numerovia;
                        document.getElementById("id_floor").value=guardian.piso;
                        document.getElementById("id_letter").value=guardian.letra;
                        document.getElementById("id_cp").value=guardian.cp;
                        document.getElementById("id_city").value=guardian.ciudad;
                        document.getElementById('id_phonenumber').value=guardian.numero;
                      //   document.getElementById('email').value=guardian.value;            
            },
        failure:function(data){
            createalert("Se ha producido un error durante la operación.");
        }

})
})

function enabledataedition(){
    
    document.getElementById("clickerformdata").style.display="block";
    document.getElementById("editor-closer").style.display="block";
    for(input of allinputs){
        input.disabled=false;
    }

    for(select of allselects){
        select.disabled=false;
    }


}

function disabledataedition(){
    document.getElementById("clickerformdata").style.display="none";
    document.getElementById("editor-closer").style.display="none";
    for(input of allinputs){
        input.disabled=true;
    }

    for(select of allselects){
        select.disabled=true;
    }
}