from django.urls import path
from . import views

app_name = 'engine'

urlpatterns = [
    path('credit_score/',views.credit_score,name = 'c_score'),
    path('eligibility_score/',views.eligibility_score,name = 'e_score'),

]
