from django.db import models
from users.models import Customer


class Company(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
    url = models.URLField(verbose_name='Company\'s Link', max_length=500, blank=True, null=True)
    logo = models.ImageField(upload_to='media/company_logos', blank=True, null=True)
        

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"

class CompanyAddress(models.Model):
    owner = models.ForeignKey(Customer, related_name='companies', on_delete=models.CASCADE)
    company = models.ForeignKey(Company, related_name='address', on_delete=models.CASCADE)
    address = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    postal = models.CharField(verbose_name='postal/ZIP code', max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    

    class Meta:
        verbose_name = "Company address"
        verbose_name_plural = "Company addresses"

class Account(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True) 
    description = models.CharField(max_length=300, blank=True, null=True)
    balance = models.DecimalField(blank=True, null=True, default=0.000, decimal_places=3)
    account_number = models.IntegerField(blank=True, null=True, max_length=50)
    holder = models.ForeignKey(Customer, related_name='account', on_delete=models.CASCADE)
    bank_url = models.URLField(verbose_name=' Internet banking link', blank=True, null=True)

    def __str__(self):
        return 

class Deposit(models.Model):
    account = models.ForeignKey('Account', related_name='deposits', on_delete=models.CASCADE)
    date = models.DateField(blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    file = models.FileField(upload_to='media/documents/deposits', blank=True, null=True)
    ammount = models.DecimalField(decimal_places=3, blank=True, null=True)


    def __str__(self):
        return f'{self.account} deposited {self.ammount}' 

    def save(self, *args, **kwargs):
       self.account.balance = self.account.balance + self.ammount
       super(Deposit, self).save(*args, **kwargs) # Call the real save() method



class Expenses(models.Model):
    account = models.ForeignKey('Account', related_name='expenses', on_delete=models.CASCADE)
    date = models.DateField(blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    file = models.FileField(upload_to='media/documents/expenses', blank=True, null=True)
    ammount = models.DecimalField(decimal_places=3, blank=True, null=True)


    def __str__(self):
        return f'{self.account} spent {self.ammount}' 

    def save(self, *args, **kwargs):
       self.account.balance = self.account.balance - self.ammount
       super(Expenses, self).save(*args, **kwargs) # Call the real save() method



class Transfer(models.Model):
    from_ac = models.ForeignKey('Account', related_name='transfer_to', on_delete=models.CASCADE)
    to_ac = models.ForeignKey('Account', related_name='recieved_from', on_delete=models.CASCADE)
    description = models.CharField(max_length=200, blank=True, null=True)
    ammount = models.DecimalField(decimal_places=3, blank=True, null=True)

    def __str__(self):
        return f'Transferred {self.ammount} from {self.from_ac} to {self.to_ac}'
    
    def save(self, *args, **kwargs):
       self.to_ac.balance = self.to_ac.balance + self.ammount
       self.from_ac.balance = self.from_ac.balance - self.ammount
       super(Transfer, self).save(*args, **kwargs) # Call the real save() method

