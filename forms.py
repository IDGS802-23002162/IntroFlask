from wtforms import Form
from wtforms import StringField, IntegerField, PasswordField
from wtforms import EmailField 
from wtforms import validators

class UserForm(Form):
    matricula=IntegerField('Matricula', [
        validators.DataRequired(message="El campo es requerido"),
        validators.NumberRange(min=100, max=1000, message='Ingrese un valor valido')
        ]
    )
    nombre=StringField('Nombre', [
        validators.DataRequired(message="El campo es requerido"),
        validators.length(min=3, max=10, message='Ingrese nombre valido')])
    apaterno=StringField('Apaterno', [
        validators.DataRequired(message="El campo es requerido")])
    amaterno=StringField('Amaterno', [
        validators.DataRequired(message="El campo es requerido")])
    correo=EmailField('Correo', [
        validators.Email(message="Ingrese un correo valido")])

class CineForm(Form):
   
    nombre=StringField('Nombre', [
        validators.DataRequired(message="El campo es requerido"),
        validators.length(min=3, max=10, message='Ingrese nombre valido')])
    compradores=IntegerField('Compradores', [
        validators.DataRequired(message="El campo es requerido"),
        validators.NumberRange(min=1, max=1000, message='Ingrese un valor valido')])
    cantidad=IntegerField('Cantidad', [
        validators.DataRequired(message="El campo es requerido"),
        validators.NumberRange(min=1, max=1000, message='Ingrese un valor valido')])


