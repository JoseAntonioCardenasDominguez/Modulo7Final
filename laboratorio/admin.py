from django.contrib import admin
from .models import Laboratorio, DirectorGeneral, Producto

class LaboratorioAdmin(admin.ModelAdmin):
    list_display = ('clave_id', 'nombre')  

class DirectorGeneralAdmin(admin.ModelAdmin):
    list_display = ('get_clave_id', 'nombre', 'get_laboratorio') 

    def get_clave_id(self, obj):
        return obj.laboratorio.clave_id  # Retorna 
    get_clave_id.admin_order_field = 'laboratorio__clave_id'  # Permite ordenar  
    get_clave_id.short_description = 'Clave ID'  # Nombre a mostrar 

    def get_laboratorio(self, obj):
        return obj.laboratorio.nombre  # Retorna el nombre del laboratorio
    get_laboratorio.admin_order_field = 'laboratorio'  # Permite ordenar 
    get_laboratorio.short_description = 'Laboratorio'  # Nombre a mostrar  

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'get_laboratorio', 'f_fabricacion', 'p_costo', 'p_venta')  # Cambia 'laboratorio' por 'get_laboratorio'

    def get_laboratorio(self, obj):
        return obj.laboratorio.nombre  # Retorna solo el nombre del laboratorio
    get_laboratorio.admin_order_field = 'laboratorio'  # Permite ordenar por laboratorio
    get_laboratorio.short_description = 'Laboratorio'  # Nombre a mostrar en el encabezado

admin.site.register(Laboratorio, LaboratorioAdmin)
admin.site.register(DirectorGeneral, DirectorGeneralAdmin)
admin.site.register(Producto, ProductoAdmin)

# Personaliza  
admin.site.site_header = "FABRICACIÓN DE PRODUCTOS FARMACÉUTICOS"
admin.site.site_title = "Laboratorio"
admin.site.index_title = "Bienvenido al panel de administración del Laboratorio"
