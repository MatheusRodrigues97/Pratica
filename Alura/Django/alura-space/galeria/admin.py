from django.contrib import admin
from galeria.models import Fotografia

class ListandoFotografias(admin.ModelAdmin):
    
    list_display = ('id', 'nome')
    list_display_links = ('id', 'nome')

admin.site.register(Fotografia, ListandoFotografias)
