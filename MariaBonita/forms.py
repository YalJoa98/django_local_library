from django import forms
from django.utils.translation import gettext as _
from django.contrib.auth.models import User


class FormularioRegistro(forms.Form):
    nombres = forms.CharField(label='Nombres:',max_length=50,required=True)
    apellidos = forms.CharField(label='Apellidos:',max_length=30,required=True)
    correoElectronico = forms.CharField(label='Correo Electronico:',required=True)
    contrasena = forms.CharField(label='Contraseña:',widget=forms.PasswordInput,required=True)
    repetirContrasena = forms.CharField(label='Repetir Contraseña:',widget=forms.PasswordInput,required=True)

    nombres.widget = forms.TextInput(attrs={'class':'form-control'})
    apellidos.widget = forms.TextInput(attrs={'class':'form-control'})
    correoElectronico.widget = forms.TextInput(attrs={'class':'form-control','type':'email'})
    contrasena.widget = forms.TextInput(attrs={'class':"form-control",'type':"password"})
    repetirContrasena.widget = forms.TextInput(attrs={'class':"form-control",'type':"password"})

    #https://docs.djangoproject.com/en/2.0/ref/forms/validation/
    def clean(self):
        limpiarDatos = super(FormularioRegistro,self).clean()
        contrasena = limpiarDatos.get("contrasena")
        confirmarContrasena = limpiarDatos.get("repetirContrasena")
        usuario = limpiarDatos.get("correoElectronico")
        try:
            usuario = User.objects.get(username=limpiarDatos.get('correoElectronico'))
        except User.DoesNotExist:
            usuario = None

        if usuario is not None:
            raise forms.ValidationError(
                _('Correo electronico en uso')
            )
        if contrasena != confirmarContrasena:
            raise forms.ValidationError(
                _('Contraseñas no coinciden')
            )

class FormularioAcceso(forms.Form):
    correoElectronico = forms.CharField(label='Correo Electronico:', required=True)
    contrasena = forms.CharField(label='Contraseña:', widget=forms.PasswordInput, required=True)

    correoElectronico.widget = forms.TextInput(attrs={'class':'form-control','type':'email'})
    contrasena.widget = forms.TextInput(attrs={'class': "form-control", 'type': "password"})

    def clean(self):
        limpiarDatos = super(FormularioAcceso,self).clean()
        try:
            usuario = User.objects.get(username=limpiarDatos.get('correoElectronico'))
        except User.DoesNotExist:
            usuario = None
        if usuario is not None:
            if not usuario.check_password(limpiarDatos.get('contrasena')):
                raise forms.ValidationError(
                    _('Contraseña Incorrecta')
                )
        else:
            raise forms.ValidationError(
                _('Usuario no registrado')
            )