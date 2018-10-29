from django.shortcuts import render
from django.http import HttpResponseRedirect,Http404
from .forms import UserRegistrationForm,PersonalInfoForm,CurrentLoanFormset,CompletedLoanFormset,NameForm
from django.urls import reverse
from django import forms
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,get_user_model
from django.contrib.auth import login as ulogin
from rolepermissions.roles import assign_role
from CreditSols.roles import Customer
from rolepermissions.checkers import has_role
from django.db import transaction
from .models import PersonalAccount,PersonalInfo



# Create your views here.
def signup(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(data=request.POST)
        if user_form.is_valid() and user_form.cleaned_data['password1'] == user_form.cleaned_data['password2']:
            user = user_form.save()
            user.set_password(user_form.cleaned_data['password1'])
            user.save()
            t = PersonalAccount(user = user)
            t.save()
            assign_role(user,Customer)
            messages.success(request,('Registration complete'))
            return HttpResponseRedirect(reverse('personal:signup'))
        elif user_form.data['password1'] != user_form.data['password2']:
            messages.error(request,('Passwords do not match'))
        else:
            messages.error(request,user_form.errors)
    else:
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('engine:c_score'))
        else:
            user_form = UserRegistrationForm()
    return render(request,'accounts/user_registration.html',
                         {'user_form':user_form,})


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active and has_role(user,Customer):
                ulogin(request,user)
                return HttpResponseRedirect(reverse('engine:c_score'))
            else:
                messages.error(request,"Your account is not active")
                return render(request,'accounts/user_login.html')
        else:
            messages.error(request,"Invalid Username or Password")
            return render(request,'accounts/user_login.html')
    else:
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('engine:c_score'))
        else:
            return render(request,'accounts/user_login.html')


@login_required
@transaction.atomic
def update_profile(request):
    user = request.user
    if has_role(user,Customer):
        if request.method == 'POST':
            name_form = NameForm(request.POST, instance=request.user)
            personal_form = PersonalInfoForm(request.POST, instance=PersonalAccount(user).personalinfo)
            current_formset = CurrentLoanFormset(request.POST, prefix = "current_loan", instance=PersonalAccount.objects.all().filter(user=request.user)[0])
            completed_formset = CompletedLoanFormset(request.POST, prefix = "completed_loan", instance=PersonalAccount.objects.all().filter(user=request.user)[0])
            if name_form.is_valid() and personal_form.is_valid() and current_formset.is_valid() and completed_formset.is_valid():
                name_form.save()
                personal_form.save()
                for form1 in current_formset:
                    current_formset.save()
                for form2 in completed_formset:
                    completed_formset.save()
                messages.success(request,('Your profile was successfully updated!'))
                return HttpResponseRedirect(reverse('personal:profile_form'))
            else:
                messages.error(request,(name_form.errors,personal_form.errors,current_formset.errors,completed_formset.errors))
        else:
            name_form = NameForm(instance=request.user)
            personal_form = PersonalInfoForm(instance=PersonalAccount(user).personalinfo)
            current_formset = CurrentLoanFormset(prefix = "current_loan", instance=PersonalAccount.objects.all().filter(user=request.user)[0])
            completed_formset = CompletedLoanFormset(prefix = "completed_loan", instance=PersonalAccount.objects.all().filter(user=request.user)[0])
        return render(request, 'profile_form.html',
                              {'name_form': name_form,
                               'personal_form': personal_form,
                               'current_formset':current_formset,
                               'completed_formset':completed_formset,})
    else:
        raise Http404
