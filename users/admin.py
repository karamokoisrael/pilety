from django.contrib import admin
from users.models import (User, UserAddress,
                          )

class UserAddressAdmin(admin.StackedInline):
    model = UserAddress


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    '''Admin View for User'''
    list_display = ('id', 'username', 'email', 'telephone', )
    # list_filter = ('is_staff', 'is_active')
    search_fields = ('username', 'email', 'telephone', )
  
    inlines = [
        UserAddressAdmin,
    ]
   

    class Meta:
        model = User

