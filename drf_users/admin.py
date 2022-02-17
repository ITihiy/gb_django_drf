from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import DRFUser


class DRFUserAdmin(UserAdmin):
    model = DRFUser
    list_display = ['email', 'username', 'first_name', 'last_name', 'is_staff']


admin.site.register(DRFUser, DRFUserAdmin)
