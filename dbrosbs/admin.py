from django.contrib import admin
from dbrosbs.models import *

class NameOption(admin.ModelAdmin):
	list_display = ('cognome_nome', 'luogo_nascita', 'data_nascita', 'residenza','association')

admin.site.register(Name, NameOption)
admin.site.register(Association)
admin.site.register(Area)
admin.site.register(Ambit)
admin.site.register(Fascicles)
