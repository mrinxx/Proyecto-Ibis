from django import forms

from django.core.validators import RegexValidator
from datetime import date, datetime
from django.core.exceptions import ValidationError


date_format_validator= RegexValidator(r"[12]\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])", "Your string should contain letter A in it.")
def validate_age(value):
    newdate = datetime.strptime(value, '%Y-%m-%d')
    actual=date.today()
    if(actual.year-newdate.year<18):
        raise ValidationError(
            "La fecha de nacimiento no es válida, el usuario debe ser mayor de edad"
        )
class LoginForm(forms.Form):
    username=forms.CharField(label='Nombre de usuario',required=True)
    password= forms.CharField(label='Contraseña:', widget=forms.PasswordInput)


VIA_TYPES=[
     ("Calle","Calle"),
     ("Avenida","Avenida"),
     ("Callejón","Callejón"),
     ("Bulevar","Bulevar"),
     ("Camino","Camino")
     ]

class teacherPersonalDataChangeForm(forms.Form):
    birthdate=forms.CharField(label="Fecha de nacimiento",widget=forms.DateInput,required=True,validators=[date_format_validator,validate_age])
    viatype = forms.ChoiceField(choices=VIA_TYPES,required=True,label="Tipo de via:")
    vianame=forms.CharField(label="Nombre de via:",required=True)
    vianumber=forms.IntegerField(label="Numero:",required=True)
    floor=forms.IntegerField(label="Piso",required=True)
    letter=forms.CharField(label="Letra",max_length=1,min_length=1,required=True)
    cp=forms.IntegerField(label="CP:",required=True)
    city=forms.CharField(label="Ciudad",required=True)

class personalDataChangeForm(forms.Form):
    birthdate=forms.CharField(label="Fecha de nacimiento",widget=forms.DateInput,required=True,validators=[date_format_validator,validate_age])
    viatype = forms.ChoiceField(choices=VIA_TYPES,required=True,label="Tipo de via:")
    vianame=forms.CharField(label="Nombre de via:",required=True)
    vianumber=forms.IntegerField(label="Numero:",required=True)
    floor=forms.IntegerField(label="Piso",required=True)
    letter=forms.CharField(label="Letra",max_length=1,min_length=1,required=True)
    cp=forms.IntegerField(label="CP:",required=True)
    city=forms.CharField(label="Ciudad",required=True)
    phonenumber=forms.CharField(label="Numero de teléfono:",min_length=9,max_length=9,required=True,widget=forms.NumberInput)


   