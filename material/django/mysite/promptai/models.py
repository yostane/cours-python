from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Prompt(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    query = models.CharField(max_length=200)
    reply = models.CharField(max_length=2000)

    def __str__(self) -> str:
        return f"Prompt of {self.user.username}: {self.user.query}. The reply was: {self.user.reply}"
