from django.contrib import admin

# Register your models here.
from django.contrib import admin
from user.models import User

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email']
    list_display_links = ['id', 'username', 'email']


admin.site.register(User, UserAdmin)