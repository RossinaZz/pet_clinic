from django import forms

class ClientFormulario(forms.Form):

    nombre= forms.CharField()
    apellido= forms.CharField()
    email= forms.EmailField()
    numerocliente= forms.IntegerField()
  