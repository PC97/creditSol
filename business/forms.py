from django import forms
from django.contrib.auth import get_user_model
from .models import UploadFile
from .validators import vpassword,validate_email_unique,validate_name_unique,validate_name_case



# Create your forms here.
class BankRegistrationForm(forms.ModelForm):
    username = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control',
                                                                  'placeholder':'Bank Code'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control',
                                                            'placeholder':'Bank Email'}),
                                                            validators=[validate_email_unique])
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control',
                                                               'placeholder':'Bank Name',}),
                                                               validators=[validate_name_unique,validate_name_case])
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control',
                                                                'placeholder':'Password'}),
                                                                validators=[vpassword])
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control',
                                                                'placeholder':'Verify Password'}))

    class Meta:
        model = get_user_model()
        fields = ('username','email','first_name','password1','password2')

class UploadFileForm(forms.ModelForm):
    cir = forms.FileField(widget=forms.FileInput(attrs={'class':'form-control-file'}))

    class Meta:
        model = UploadFile
        fields = ('cir',)
