from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.homepage,name = 'home'),
    path('howitworks/',views.HowItWorks.as_view(),name = 'howitworks'),
    path('helpcenter/',views.HelpCenter.as_view(),name = 'helpcenter'),
    path('logout/',views.logout,name = 'logout'),
    path('thanks/',views.Thanks.as_view(),name = 'thanks'),
    path('personal/',include('personal.urls',namespace='personal')),
    path('business/',include('business.urls',namespace='business')),
    path('engine/',include('engine.urls',namespace='enigne')),
]
