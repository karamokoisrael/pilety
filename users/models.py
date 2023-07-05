from django.db import models
from django.contrib.auth.models import AbstractBaseUser, Group, BaseUserManager 
from choices import PAY_TYPE_CHOICES, DRIVER_STATUS_CHOICES
from django.contrib.auth.models import AbstractUser


from django.db import models

# class CustomUserManager(BaseUserManager):
#     def create_user(self, email, password=None, **extra_fields):
#         if not email:
#             raise ValueError('The Email field must be set')
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)

#         if extra_fields.get('is_staff') is not True:
#             raise ValueError('Superuser must have is_staff=True.')
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError('Superuser must have is_superuser=True.')

#         return self.create_user(email, password, **extra_fields)
    
   
    

class User(AbstractUser):
    # USERNAME_FIELD = 'username'
    # REQUIRED_FIELDS = ['email',] 
    username = models.CharField(help_text='Write a unique username', 
                                verbose_name= 'User name',
                                max_length=90,unique=True,
                                blank=True, null=True)
    
    telephone = models.CharField(max_length=100, blank=True, null=True
                                )
    email = models.EmailField(max_length=240, blank=True, null=True, unique=True)

    is_active = models.BooleanField(default=True)

    is_staff = models.BooleanField(default=False)
    
    img = models.ImageField(verbose_name='Image',upload_to='media/users', 
                            help_text='If you are a supplier upload your business card here',
                            max_length=None, blank=True, null=True)
    
    notes = models.TextField(blank=True, null=True)

    # objects = CustomUserManager()

    def __str__(self):
        return self.username
    
    
 
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
