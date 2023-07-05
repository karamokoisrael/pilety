from django.db import models
from django.contrib.auth.models import AbstractBaseUser, Group
from choices import PAY_TYPE_CHOICES, DRIVER_STATUS_CHOICES


class User(AbstractBaseUser):
    USERNAME_FIELD = 'username'
    username = models.CharField(help_text='Write a unique username', 
                                verbose_name= 'User name',
                                max_length=90,unique=True,
                                blank=True, null=True)
    
    telephone = models.CharField(max_length=100, blank=True, null=True
                                )
    email = models.EmailField(max_length=240, blank=True, null=True)
    
    img = models.ImageField(verbose_name='Image',upload_to='media/users', 
                            help_text='If you are a supplier upload your business card here',
                            max_length=None, blank=True, null=True)
    notes = models.TextField(blank=True, null=True
                             )
    
    
 
class UserAddress(models.Model):
    user = models.ForeignKey('User', related_name='address',
                                  on_delete=models.CASCADE
                                  )
    address = models.CharField(max_length=100, blank=True, null=True
                                )
    city = models.CharField(max_length=100, blank=True, null=True
                            )
    def __str__(self):
        return f'{self.user}\'s + {self.address}'
    
    class Meta:
        verbose_name = "User's Address"
        verbose_name_plural = "User's Addresses"
