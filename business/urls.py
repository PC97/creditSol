from django.urls import path
from . import views

app_name = 'business'

urlpatterns = [
    path('login/',views.login,name = 'login'),
    path('signup/',views.signup,name='signup'),
    path('dashboard/',views.dashboard,name = 'dashboard'),
    path('upload/',views.upload,name = 'upload'),
]
