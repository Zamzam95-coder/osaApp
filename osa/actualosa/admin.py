from django.contrib import admin
from .models import Command
# Register your models here.

@admin.register(Command)
class CommandAdmin(admin.ModelAdmin):
    pass