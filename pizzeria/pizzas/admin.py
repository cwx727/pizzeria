from django.contrib import admin
from .models import *

# Register your models here.

class ToppingAdmin(admin.ModelAdmin):
	list_display = ['pizza', 'name']

admin.site.register(Pizza)
admin.site.register(Topping, ToppingAdmin)
