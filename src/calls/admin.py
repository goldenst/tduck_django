from django.contrib import admin


from .models import Call
from .models import Cart

admin.site.register(Call)
admin.site.register(Cart)
