from django import forms



# Create your forms here.
class EligibilityForm(forms.Form):
    TYPE = (
        ('C','Choose'),
        ('Home', 'Home Loan'),
        ('Student', 'Student Loan'),
        ('Personal', 'Personal Loan'),
        ('Vehicle', 'Vehicle Loan'),
    )
    tenure = forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control',}))
    rate = forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control',}))
    type = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control',}),choices=TYPE)
