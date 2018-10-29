from django import forms
from django.contrib.auth import get_user_model
from .validators import vpassword,validate_email_unique
from .models import PersonalInfo,CurrentLoan,CompletedLoan,PersonalAccount
from django.forms import inlineformset_factory



# Create your forms here.
class UserRegistrationForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control',
                                                             'placeholder':'Username'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control',
                                                           'placeholder':'Email'}),
                                                            validators=[validate_email_unique])
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control',
                                                               'placeholder':'First Name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control',
                                                              'placeholder':'Last Name'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control',
                                                                'placeholder':'Password'}),
                                                                validators=[vpassword])
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control',
                                                                'placeholder':'Verify Password'}))
    class Meta:
        model = get_user_model()
        fields = ('username','email','first_name','last_name','password1','password2')



class NameForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control',}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control',}))
    class Meta:
        model = get_user_model()
        fields = ('first_name','last_name',)



class PersonalInfoForm(forms.ModelForm):
    GENDER = (
        ('C','Choose'),
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control',}),choices=GENDER)
    phone = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control',}))
    aadhar_number = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control',}))
    pan_number = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control',}))
    address = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control',}))
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control','id':"date",}))
    monthly_income = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control',}))
    average_monthly_savings = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control',}))
    class Meta:
        model = PersonalInfo
        fields = ('gender','phone','aadhar_number','pan_number','address','date_of_birth','monthly_income','average_monthly_savings')


CurrentLoanFormset = inlineformset_factory(
    PersonalAccount,
    CurrentLoan,
    fields = ('current_bank','current_amount','current_length','current_interest','current_duration',),
    extra=1,
    widgets={'current_bank': forms.TextInput(attrs={
             'class':'form-control',
            }),
            'current_amount': forms.NumberInput(attrs={
            'class':'form-control',
            }),
            'current_length': forms.NumberInput(attrs={
            'class':'form-control',
            }),
            'current_interest': forms.NumberInput(attrs={
            'class':'form-control',
            }),
            'current_duration': forms.NumberInput(attrs={
            'class':'form-control',
            }),
    }
)


CompletedLoanFormset = inlineformset_factory(
    PersonalAccount,
    CompletedLoan,
    fields = ('comp_bank','comp_amount','comp_length','comp_interest',),
    extra=1,
    widgets={'comp_bank': forms.TextInput(attrs={
             'class':'form-control',
            }),
            'comp_amount': forms.NumberInput(attrs={
            'class':'form-control',
            }),
            'comp_length': forms.NumberInput(attrs={
            'class':'form-control',
            }),
            'comp_interest': forms.NumberInput(attrs={
            'class':'form-control',
            }),
    }
)
