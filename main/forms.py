from django import forms
from .models import Doctors, Post, Message, Contact

class PostCreateForm(forms.ModelForm):
    class Meta: 
        model = Post
        fields = ['title', 'content']
        labels = {
            'title':'Naglówek',
            'content':'Treść'
        }
        widgets = {
            'title':forms.TextInput(attrs={
                'class':'form-control'}), 
            'content':forms.TextInput(attrs={
                'class':'form-control'}), 
        }
        error_messages = {
            'title': {
                'required': 'To pole jest wymagane.',
                'max_length': 'Maksymalna długość to 200 znaków.'
            },
            'content': {
                'required': 'To pole jest wymagane.'
            }
        }