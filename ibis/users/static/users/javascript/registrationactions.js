let guardian;//alamcena el tutor que se esta intentando dar de alta en la plataforma
function Guardian(codigo,username,password,dni,nombre,apellidos,nacimiento,direccion,email,numero,acuerdoprivacidad,terminos,newsletter,activado,imagen){
    this.codigo=codigo;
    this.username=username;
    this.password=password;
    this.dni=dni;
    this.nombre=nombre;
    this.apellidos=apellidos;
    this.nacimiento=nacimiento;
    this.direccion=direccion;
    this.email=email;
    this.numero=numero;
    this.acuerdoprivacidad=acuerdoprivacidad;
    this.terminos=terminos;
    this.newsletter=newsletter;
    this.activado=activado;
    this.imagen=imagen;
}

//con esta función se buscará el código del usuario para así obtener los datos y que se muestren
function getusercode(elemento){
    let code=elemento.value;
    if(code==""){
        cleaninputs();
    }
    if(code.length==10){
        $.ajax({
            url:'/users/guardiandetails',
            method:"GET",
            data:{"code":code},
            dataType:'json',
            success:function(data){
                let jsonGuardian=JSON.parse(data.guardian);
                
                //establezco guardian de tipo Guardian para poder acceder más facilmente a los datos que debe de
                //tener el tutor de los alumnos
                if(jsonGuardian.length==0){
                    document.getElementById("usercode").value="";
                    createalert("El usuario con ese código no existe.");
                    cleaninputs();
                }
                else{
                guardian=new Guardian(
                    jsonGuardian[0].pk,
                    jsonGuardian[0].fields.guardianusername,
                    jsonGuardian[0].fields.password,
                    jsonGuardian[0].fields.dni,
                    jsonGuardian[0].fields.name,
                    jsonGuardian[0].fields.last_name,
                    jsonGuardian[0].fields.birth_date,
                    jsonGuardian[0].fields.address,
                    jsonGuardian[0].fields.email,
                    jsonGuardian[0].fields.phone,
                    jsonGuardian[0].fields.privacity,
                    jsonGuardian[0].fields.terms,
                    jsonGuardian[0].fields.newsletter,
                    jsonGuardian[0].fields.activated,
                    jsonGuardian[0].fields.image
                    );
                    if(guardian.activado=="si"){
                        document.getElementById("usercode").value="";
                        createalert("El usuario con ese código ya está activado.");
                        cleaninputs();
                    }
                    else{
                        document.getElementById('dni').value=guardian.dni;
                        document.getElementById('name').value=guardian.nombre;
                        document.getElementById('username').value=guardian.username;
                        document.getElementById('lastname').value=guardian.apellidos;
                        document.getElementById('birth-date').value=guardian.nacimiento;
                        document.getElementById('address').value=guardian.direccion;
                        document.getElementById('email').value=guardian.email;
                        document.getElementById('phonenumber').value=guardian.numero;
    
                    }
                }
            },
            failure:function(data){
                createalert("Se ha producido un error durante la operación.");
            }
        })
    }
    
}

function createalert(text){
    let divalerta=document.getElementById("alerta");
   document.getElementById("message").textContent=text;  
   divalerta.style="display:block;border: 3px solid black;text-align: center;width: 85.5%;height:70px;margin: auto;border-radius: 10px;background-color: #FAA81D;font-weight: 800;margin-bottom:5%"           
        
        setTimeout(() => {
          divalerta.style="display:none";
        }, 5000);
}

function validatepasswords(){
    let password=document.getElementById("password");
    let repetition=document.getElementById("passwordrepetition");
    if(password.length!=repetition.length || password.value!=repetition.value){
        createalert("Las contraseñas introducidas no coinciden. Inténtelo de nuevo");
        document.getElementById('pagetitle').scrollIntoView(); //para que vaya a mostrar el mensaje
        password.value="";
        repetition.value="";
    }
}


// function process(){
//     if($("#comunications").prop('checked')){
//         guardian.newsletter="si";
//     }else{
//         guardian.newsletter="no";
//     }
//     guardian.password=$("#password").val();
//     guardian.terms="si";
//     guardian.privacity="si";
//     guardian.imagen=$("#userimage").val();

//     let csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
//     $.ajax({
//         headers: {'X-CSRFToken': csrftoken},
//         url:'/users/register',
//         method:"POST",
//         data:{
//             'usercode':guardian.codigo,
//             'image':guardian.imagen,
//             'phonenumber':guardian.numero,
//             'email':guardian.email,
//             'address':guardian.direccion,
//             'privacitypolicy':guardian.privacity,
//             'comunications':guardian.newsletter,
//             'terms':guardian.terms,
//         },
//         dataType:'json',
//         success:function(data){
//             console.log(data);
//         },
//         failure:function(data){
//             console.log(data);
//         }
//     })
// }

function cleaninputs(){
    document.querySelectorAll("input").forEach(input => {
        input.value="";
        
    });
}

