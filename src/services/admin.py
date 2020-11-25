from django.contrib import admin
gi

from .models import Service


class ServiceAdmin(admin.ModelAdmin):
    list_display = ( '__str__','slug','rate')
    class Meta:
        model = Service
    

admin.site.register(Service, ServiceAdmin)
