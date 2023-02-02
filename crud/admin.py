from django.contrib import admin
from .models import Registration

# Register your models here.
@admin.register(Registration)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone','photo', 'date')
