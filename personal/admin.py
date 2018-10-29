from django.contrib import admin
from personal.models import PersonalInfo,CurrentLoan,CompletedLoan,DuesInfo
# Register your models here.

admin.site.register(PersonalInfo)
admin.site.register(CurrentLoan)
admin.site.register(CompletedLoan)
admin.site.register(DuesInfo)
