from django.contrib import admin
from .models import Categoria, Producto, Embarque

class EmbarqueAdmin(admin.ModelAdmin):
    filter_horizontal = ('productos',)

admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Embarque, EmbarqueAdmin)