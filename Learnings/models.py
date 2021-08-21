from django.db import models

# Create your models here.
class Login(models.Model):
    Username = models.CharField(max_length=10, blank=False, null=False)
    Password = models.CharField(max_length=10, blank=False, null=False)

    class Meta:
        verbose_name_plural = 'Login'
