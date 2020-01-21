from django.contrib import admin

# Register your models here.
from .models import resident, federal , visitor

admin.site.register(resident)
admin.site.register(federal)
admin.site.register(visitor)