from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
import re

def vpassword(value):
    flag = 0
    while True:
        if (len(value)<8):
            flag = -1
            break
        elif not re.search("[a-z]", value):
            flag = -1
            break
        elif not (re.search("[A-Z]", value) or re.search("[! , @ , # , $ , % , ^ , & , * , - , _ , + , =]", value)):
            flag = -1
            break
        elif not re.search("[0-9]", value):
            flag = -1
            break
        elif re.search("\s", value):
            flag = -1
            break
        else:
            flag = 0
            break

    if flag ==-1:
        raise ValidationError('password should have minimum 8 charecters and should have atleast 1 number and either 1 capital letter or 1 special charecter')

def validate_email_unique(value):
    exists = get_user_model().objects.filter(email=value)
    if exists:
        raise ValidationError("this email address already exists")

def validate_name_unique(value):
    exists = get_user_model().objects.filter(first_name=value)
    if exists:
        raise ValidationError("This bank is already registered")

def validate_name_case(value):
    if not re.search("[A-Z]", value):
        raise ValidationError("Bank name should be in all caps")
