from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

# Register your models here.
from .models import UserModel



class UserInline(admin.StackedInline):
	model=UserModel
	can_delete=False
	verbose_name_plural="UserModels"

class CustomizedUserAdmin(UserAdmin):
	inlines=(UserInline,)

admin.site.unregister(User) 
admin.site.register(User,CustomizedUserAdmin) 
