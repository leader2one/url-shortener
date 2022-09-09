from django.contrib import admin
from .models import Url
# Register your models here.
class Admin(admin.ModelAdmin):
    readonly_fields = ("created_at",)

admin.site.register(Url, Admin)