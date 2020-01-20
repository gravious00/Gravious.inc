from django.contrib import admin

# Register your models here.
from .models import resident, federal

admin.site.register(resident)
admin.site.register(federal)