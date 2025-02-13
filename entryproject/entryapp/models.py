from django.db import models

from accounts.models import CustomUser


# Create your models here.

class EntryModel(models.Model) :
    title = models.CharField(max_length=50)
    entry_text = models.CharField(max_length=100)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

