from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager

# Create your models here.


class TaomApi(models.Model):
    name = models.CharField(max_length = 70)
    
    def __str__(self):
        return self.name
    


class ListApi(models.Model):
    taom_turi = models.ForeignKey(TaomApi, on_delete = models.CASCADE, null =True, blank = True)
    taom_nomi_uz = models.CharField(max_length=50, null=True, blank =True)
    taom_nomi_ru = models.CharField(max_length=50, null=True, blank =True)
    taom_nomi_en = models.CharField(max_length=50, null=True, blank =True)
    taom_nomi_ar = models.CharField(max_length=50, null=True, blank =True)
    
    narx_uz = models.CharField(max_length=50, null=True, blank =True )
    narx_ru = models.CharField(max_length=50, null=True, blank =True )
    narx_en = models.CharField(max_length=50, null=True, blank =True )
    narx_ar = models.CharField(max_length=50, null=True, blank =True )
    
    des_uz = models.TextField(null=True, blank =True)
    des_ru = models.TextField(null=True, blank =True)
    des_en = models.TextField(null=True, blank =True)
    des_ar = models.TextField(null=True, blank =True)
    
    img=models.ImageField(upload_to='images/', null=True)
    
    
    def __str__(self):
        return self.taom_nomi_uz
    
    