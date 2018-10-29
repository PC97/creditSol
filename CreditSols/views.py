from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from .roles import Banker,Customer
from django.shortcuts import render
from rolepermissions.checkers import has_role

def homepage(request):
    user = request.user
    if request.user.is_authenticated:
        if has_role(user,Banker):
            return HttpResponseRedirect(reverse('business:dashboard'))
        elif has_role(user,Customer):
            return HttpResponseRedirect(reverse('engine:c_score'))
    else:
        return render(request,'index.html')

class HowItWorks(TemplateView):
    template_name = 'howitworks.html'

class HelpCenter(TemplateView):
    template_name = 'helpcenter.html'

class Thanks(TemplateView):
    template_name = 'thanks.html'

@login_required
def logout(request):
    auth_logout(request)
    return HttpResponseRedirect(reverse('thanks'))
