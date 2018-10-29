from django.db import models
from django.contrib.auth import get_user_model
from datetime import datetime



# Create your models here.
class BusinessAccount(models.Model):
    user = models.OneToOneField(
        get_user_model(),
        on_delete=models.CASCADE,
        primary_key=True,
    )

    def __str__(self):
        return self.user.first_name

current_month = (datetime.now()).strftime("%B")
def user_directory_path(instance, filename):
    user = instance.user.user.first_name
    return 'CIR/{0}/{1}/{2}'.format(user, current_month, filename)

class UploadFile(models.Model):
    user = models.ForeignKey(
        BusinessAccount,
        on_delete=models.CASCADE,
    )
    cir = models.FileField(null = False, upload_to=user_directory_path)

    def __str__(self):
        return '{0} ({1})'.format(self.user.user.first_name,current_month)
