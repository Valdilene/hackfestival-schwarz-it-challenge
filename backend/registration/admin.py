from django.contrib import admin

from .models import RegistrationProfile


# Register your models here.

class RegistrationProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')


admin.site.register(RegistrationProfile, RegistrationProfileAdmin)
