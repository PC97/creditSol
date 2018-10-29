from django.db import models
from personal.models import PersonalAccount
# Create your models here.
class Score(models.Model):
    user = models.OneToOneField(
        PersonalAccount,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    credit_score = models.CharField(max_length = 3,null = True)

    def __str__(self):
        return self.user.user.username
