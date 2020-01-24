from django.contrib import admin

# Register your models here.
from .models import resident, federal , visitor, notifiy

admin.site.register(resident)
admin.site.register(federal)
admin.site.register(visitor)
admin.site.register(notifiy)