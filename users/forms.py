from django import forms
from .models import CustomUser
from django.contrib.auth import authenticate, get_user_model


class UserCreationForm(forms.ModelForm):
    password_confirmation = forms.CharField(label='Powtórz hasło', widget=forms.PasswordInput(attrs={
        'class':'form-control'
    }))
    
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name', 'password')
        labels = {
            'username':'Nickname',
            'email':'Email', 
            'password':'Hasło', 
            'first_name':'Imię', 
            'last_name':'Nazwiśko',
        }
        widgets = {
            'username': forms.TextInput(attrs={
                'class':'form-control'
            }),
            'email': forms.TextInput(attrs={
                'class':'form-control'
            }),
            'first_name': forms.TextInput(attrs={
                'class':'form-control'
            }),
            'last_name': forms.TextInput(attrs={
                'class':'form-control'
            }),
            'password': forms.PasswordInput(attrs={
                'class':'form-control'
            }),

        }
        
    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        password_confirmation = cleaned_data.get('password_confirmation')
        
        if CustomUser.objects.filter(username=username).exists():
            raise forms.ValidationError('Uzytkownik o podanym loginie już istnieje')
        
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError('Użytkownik o podanym email już istnieje')
        
        if password and password_confirmation and password != password_confirmation:
            raise forms.ValidationError('Podane hasła róznią się')
        
        return cleaned_data
    

class LoginUserForm(forms.Form):
    email = forms.CharField(label='Email', widget=forms.TextInput(attrs={
        'class':'form-control',
    }))
    
    password = forms.CharField(label='Hasło', widget=forms.PasswordInput(attrs={
        'class':'form-control',
    }))
    
    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        if email and password:
            user = authenticate(email=email, password=password)
            if not user:
                raise forms.ValidationError('Nieprawidłowy email lub hasło')
        return cleaned_data
    

class SearchUserForm(forms.Form):
    email = forms.CharField(label='Podaj swoj email', widget=forms.TextInput(attrs={
        'class':'form-control',
    }))
    

class ResetPasswordForm(forms.Form):
    password = forms.CharField(label='Hasło', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
    }))
    
    password_confirmation = forms.CharField(label='Powtórż hasło', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
    }))

    def clean(self):
        cleaned_data=super().clean()
        password= cleaned_data.get('password')
        password_confirmation = cleaned_data.get('password_confirmation')
        
        if password and password_confirmation and password != password_confirmation:
            raise forms.ValidationError('Podane hasła róznią się')
        
        return cleaned_data
    

class InfoUpdateUserForm(forms.ModelForm):
        
    class Meta:
        model = CustomUser
        fields = ['profile_picture', 'first_name', 'last_name']
        labels = {
            'first_name':'Imię',
            'last_name':'Nazwiśko',
            'profile_picture': 'Zdięcie', 
        }
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class':'form-control',
            }),
            'last_name': forms.TextInput(attrs={
                'class':'form-control',
            }),
            'profile_picture': forms.ClearableFileInput(attrs={
                'class':'form-control',
            }),
        }
        
        
class UserStaffChangeForm(forms.Form):
    user_id = forms.IntegerField(widget=forms.HiddenInput())
    is_staff = forms.BooleanField(label='Is Staff', required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user_id'].widget.attrs.update({'class': 'user-id-field'})

    def clean_user_id(self):
        user_id = self.cleaned_data['user_id']
        if not get_user_model().objects.filter(pk=user_id).exists():
            raise forms.ValidationError('Nie znaleziono uzytkownika o dannym ID')
        return user_id