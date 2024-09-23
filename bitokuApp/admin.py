from django.contrib import admin
from .models import Profile, paciente, especialidad, doctor, citaMedica

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'sexo', 'telefono', 'cedula','user_group')
    list_filter = ('user__groups',)
    
    # Método para mostrar el primer nombre
    def first_name(self, obj):
        return obj.user.first_name
    first_name.short_description = 'First Name'

    # Método para mostrar el segundo nombre (apellido)
    def last_name(self, obj):
        return obj.user.last_name
    last_name.short_description = 'Last Name'

    # Método para mostrar los roles del usuario
    def user_group(self, obj):
        return " - ".join([t.name for t in obj.user.groups.all()])
    
    user_group.short_description = 'Roles'

admin.site.register(Profile, ProfileAdmin)

    
@admin.register(paciente)
class BitokuAdmin(admin.ModelAdmin):
    list_display = (
        'id', 
        'fecha_nacimiento', 
        'usuario__user__email', 
        'usuario__user__first_name', 
        'usuario__user__last_name', 
        'usuario__cedula', 
        'usuario__sexo', 
        'usuario__telefono'
    )
    ordering = ('id',)


# @admin.register(especialidad)
# class BitokuAdmin(admin.ModelAdmin):
#     list_display = ('id', 'nombre', 'institucion', 'anio_recebimiento')
#     ordering = ('id',)

# @admin.register(doctor)
# class BitokuAdmin(admin.ModelAdmin):
#     list_display = ('id', 'apellido_paterno', 'apellido_materno', 'nombres', 'sexo', 'cedula', 'telefonoDoctor', 'emailDoctor', 'especialidad')
#     ordering = ('id',)

# @admin.register(citaMedica)
# class BitokuAdmin(admin.ModelAdmin):
#     list_display = ('id', 'fechaCita', 'horaCita', 'estadoCita', 'paciente', 'doctor')
#     ordering = ('id',)