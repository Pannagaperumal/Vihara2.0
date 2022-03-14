from django.db import models

# Create your models here.
class destination(models.Model):
    name=models.CharField(max_length=100,default=0)
    img=models.ImageField(upload_to='pics',default=0)
    desc = str
    offer =models.BooleanField(default=False)
