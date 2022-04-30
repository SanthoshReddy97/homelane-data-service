from django.contrib import admin

# Register your models here.
from homes.models import Country, Home

admin.site.register(Country)
admin.site.register(Home)
