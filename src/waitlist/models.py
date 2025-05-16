from django.db import models

# Create your models here.

class WaitlistModel(models.Model):
    email = models.EmailField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.email

