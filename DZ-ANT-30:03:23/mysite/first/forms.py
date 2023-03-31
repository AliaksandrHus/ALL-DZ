from django import forms

class UserForm(forms.Form):

    name = forms.CharField(label='Ваше Имя:')
    how = forms.IntegerField(label='Сколько:')
