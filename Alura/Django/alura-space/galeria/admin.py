from django.contrib import admin
from galeria.models import Fotografia

class ListandoFotografias(admin.ModelAdmin):
    
    list_display = ('id', 'nome', 'publicada')
    list_display_links = ('id', 'nome')
    list_filter = ('categoria',)
    search_fields = ('nome',)
    list_editable = ('publicada',)
    list_per_page = 20

admin.site.register(Fotografia, ListandoFotografias)
