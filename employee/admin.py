from django.contrib import admin

# Register your models here.

from .models import Login,Register

admin.site.register(Login)
admin.site.register(Register)