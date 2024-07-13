from django import forms
from .models import Doctors, Post, Message, Contact, Rodo, Reglamin, File_to_download

class PostCreateForm(forms.ModelForm):
    class Meta: 
        model = Post
        fields = ['title', 'content', 'file']
        labels = {
            'title':'Naglówek',
            'content':'Treść',
            'file':'Dodaj grafikę'
        }
        widgets = {
            'title':forms.TextInput(attrs={
                'class':'form-control'}), 
            'content':forms.Textarea(attrs={
                'class':'form-control'}), 
            'file': forms.FileInput(attrs={
                'class': 'form-control'}),
        }
        error_messages = {
            'title': {
                'required': 'To pole jest wymagane.',
                'max_length': 'Maksymalna długość to 200 znaków.'
            },
        }
        

class DoctorCreateForm(forms.ModelForm):
    class Meta:
        model = Doctors
        fields = ['first_name', 'last_name', 'description', 'specialization', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'file_upload']
        labels = {
            'first_name': 'Imię',
            'last_name': 'Nazwisko',
            'description': 'Opis',
            'specialization': 'Specjalizacja',
            'monday': 'Poniedziałek',
            'tuesday': 'Wtorek',
            'wednesday': 'Środa',
            'thursday': 'Czwartek',
            'friday': 'Piątek',
            'file_upload': 'Plik do pobrania',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control'}),
            'description': forms.Textarea(attrs={
                'class': 'form-control'}),
            'specialization': forms.Select(attrs={
                'class': 'form-control'}),
            'monday': forms.TextInput(attrs={
                'class': 'form-control'}),
            'tuesday': forms.TextInput(attrs={
                'class': 'form-control'}),
            'wednesday': forms.TextInput(attrs={
                'class': 'form-control'}),
            'thursday': forms.TextInput(attrs={
                'class': 'form-control'}),
            'friday': forms.TextInput(attrs={
                'class': 'form-control'}),
            'file_upload': forms.FileInput(attrs={
                'class': 'form-control'}),
        }
        error_messages = {
            'first_name': {
                'required': 'Proszę podać imię.',
            },
            'last_name': {
                'required': 'Proszę podać nazwisko.',
            },
            'description': {
                'required': 'Proszę podać opis.',
            },
            'specialization': {
                'required': 'Proszę wybrać specjalizację.',
            },
            'monday': {
                'required': 'Proszę podać godziny pracy na poniedziałek.',
            },
            'tuesday': {
                'required': 'Proszę podać godziny pracy na wtorek.',
            },
            'wednesday': {
                'required': 'Proszę podać godziny pracy na środę.',
            },
            'thursday': {
                'required': 'Proszę podać godziny pracy na czwartek.',
            },
            'friday': {
                'required': 'Proszę podać godziny pracy na piątek.',
            },
            'file_upload': {
                'required': 'Proszę przesłać plik.',
            },
        }


class MessageCreateForm(forms.ModelForm):
    class Meta: 
        model = Message
        fields = ['title', 'text', 'date_start', 'date_end']
        labels = {
            'title':'Naglówek',
            'text':'Treść',
            'date_start':'Data początku', 
            'date_end':'Data konca', 
        }
        widgets = {
            'title':forms.TextInput(attrs={
                'class':'form-control'}), 
            'text':forms.Textarea(attrs={
                'class':'form-control'}), 
            'date_start':forms.DateInput(attrs={
                'class':'form-control',
                'type':'date'}), 
            'date_end':forms.DateInput(attrs={
                'class':'form-control',
                'type':'date'}), 
        }
        error_messages = {
            'title': {
                'required': 'To pole jest wymagane.',
            },
            'text': {
                'required': 'To pole jest wymagane.'
            },
            'date_start': {
                'required': 'To pole jest wymagane.'
            },
            'date_end': {
                'required': 'To pole jest wymagane.'
            }
        }
        
        
class ContactCreateForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['number_phone_1', 'number_phone_2', 'email', 'email_2', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday']
        labels = {
            'number_phone_1':'Numer kontaktowy',
            'number_phone_2':'Numer kontaktowy',
            'email':'Email do rejestracji',
            'email_2':'Email do biura',
            'monday': 'Poniedziałek',
            'tuesday': 'Wtorek',
            'wednesday': 'Środa',
            'thursday': 'Czwartek',
            'friday': 'Piątek',
        }
        widgets = {
            'number_phone_1':forms.TextInput(attrs={
                'class':'form-control'}), 
            'number_phone_2':forms.TextInput(attrs={
                'class':'form-control'}), 
            'email':forms.TextInput(attrs={
                'class':'form-control'}), 
            'monday': forms.TextInput(attrs={
                'class': 'form-control'}),
            'tuesday': forms.TextInput(attrs={
                'class': 'form-control'}),
            'wednesday': forms.TextInput(attrs={
                'class': 'form-control'}),
            'thursday': forms.TextInput(attrs={
                'class': 'form-control'}),
            'friday': forms.TextInput(attrs={
                'class': 'form-control'}),
        }
        
        error_messages = {
            'number_phone_1': {
                'required': 'To pole jest wymagane.',
            },
            'email': {
                'required': 'To pole jest wymagane.'
            },
        }
        

class RodoCreateForm(forms.ModelForm):
    class Meta:
        model = Rodo
        fields = ['text', 'file_upload']
        labels = {
            'text':'Treść',
            'file_upload':'Plik do pobrania'
        }
        wigets = {
            'text':forms.Textarea(attrs={
                'class':'form-control'
            }),
            'file_upload':forms.FileInput(attrs={
                'class':'form-control'
            })
        }
        error_messages = {
            'text': {
                'required': 'To pole jest wymagane.',
            },
            'file_upload': {
                'required': 'To pole jest wymagane.'
            },
        }
        
        
class ReglaminCreateForm(forms.ModelForm):
    class Meta:
        model = Reglamin
        fields = ['text', 'file_upload']
        labels = {
            'text':'Treść',
            'file_upload':'Plik do pobrania'
        }
        wigets = {
            'text':forms.Textarea(attrs={
                'class':'form-control'
            }),
            'file_upload':forms.FileInput(attrs={
                'class':'form-control'
            })
        }
        error_messages = {
            'text': {
                'required': 'To pole jest wymagane.',
            },
            'file_upload': {
                'required': 'To pole jest wymagane.'
            },
        }
        
        
class FileToDownloadCreateForm(forms.ModelForm):
    class Meta:
        model = File_to_download
        fields = ['rodo','reglamin','doctor','nurse','instruction','calendar','application_for_authorisation',]
        labels = {
            'rodo':'RODO',
            'reglamin':'Reglamin przychodni',
            'doctor':'Deklaracja POZ (lekarz)',
            'nurse':'Deklaracja POZ (pielęgniarka)',
            'instruction': 'Instrukcja wypelnenia deklaracji',
            'calendar': 'kalendarz szczepień',
            'application_for_authorisation':'pelnomocnictwo',
        }
        wigets = {
            'rodo':forms.FileInput(attrs={
                'class':'form-control'
            }),
            'reglamin':forms.FileInput(attrs={
                'class':'form-control'
            }),
            'doctor':forms.FileInput(attrs={
                'class':'form-control'
            }),
            'nurse':forms.FileInput(attrs={
                'class':'form-control'
            }),
            'instruction':forms.FileInput(attrs={
                'class':'form-control'
            }),
            'calendar':forms.FileInput(attrs={
                'class':'form-control'
            }),
            'application_for_authorisation':forms.FileInput(attrs={
                'class':'form-control'
            }),
        }