from django import forms

class LoginForm(forms.Form):
    username=forms.CharField(label='Nombre de usuario',required=True)
    password= forms.CharField(label='Contraseña:', widget=forms.PasswordInput)


# class GuardianUpdateForm(forms.Form):
#     VIA_TYPES=[
#      ("Calle","Calle"),
#      ("Avenida","Avenida"),
#      ("Callejón","Callejón"),
#      ("Bulevar","Bulevar"),
#      ("Camino","Camino")
#     ]
    
#     CHOICES=[('Si','Si'),
#          ('Si','No')]
#     code=forms.CharField(label="Código:",max_length=10,min_length=10)
#     dni=forms.CharField(label="DNI:",min_length=9,max_length=9,required=True)
#     birthdate=forms.CharField(label="Fecha de nacimiento",widget=forms.DateInput,required=True)
#     # password=forms.CharField(label='Contraseña:', min_length=8,max_length=20,widget=forms.PasswordInput)
#     # passwordrepetition=forms.CharField(label='Repita la contraseña:', widget=forms.PasswordInput)
#     viatype = forms.ChoiceField(choices=VIA_TYPES,required=True,label="Tipo de via:")
#     vianame=forms.CharField(label="Nombre de via:",required=True)
#     vianumber=forms.IntegerField(label="Numero:",required=True)
#     floor=forms.IntegerField(label="Piso",required=True)
#     letter=forms.CharField(label="Letra",max_length=1,min_length=1,required=True)
#     cp=forms.IntegerField(label="CP:",required=True)
#     city=forms.CharField(label="Ciudad",required=True)
#     userimage=forms.ImageField(label="Imagen:",required=False)
#     phonenumber=forms.CharField(label="Numero de teléfono:",min_length=9,max_length=9,required=True,widget=forms.NumberInput)
#     privacitypolicy= forms.BooleanField(required=True,label="He leído y acepto la política de privacidad de la empresa")
#     terms=forms.BooleanField(required=True,label="He leído y acepto los términos y condiciones")
#     comunications = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect,required=True)

   



    # VIA_TYPES=[
    #  ("Calle","Calle"),
    #  ("Avenida","Avenida"),
    #  ("Callejón","Callejón"),
    #  ("Bulevar","Bulevar"),
    #  ("Camino","Camino")
    # ]
    # CHOICES=[('Si','Si'),
    #      ('Si','No')]
    # username=forms.CharField(label="Nombre de usuario:",required=True,disabled=True)
   
    # name=forms.CharField(label="Nombre:",required=True,disabled=True)
    # lastname=forms.CharField(label="Apellidos",required=True,disabled=True)
    # email=forms.CharField(label="Correo electónico:",widget=forms.EmailInput,required=True,disabled=True)
   
    