from django.contrib import admin
from .models import Comp

# Register your models here.
class CompAdmin(admin.ModelAdmin):
    pass
admin.site.register(Comp, CompAdmin)