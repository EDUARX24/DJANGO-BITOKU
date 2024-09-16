from django.contrib import admin
from .models import usuario, paciente, especialidad, doctor, citaMedica

# Register your models here.
# admin.site.register(usuario)

@admin.register(usuario)
class BitokuAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombreUsuario', 'contrasenia', 'rol')
    ordering = ('id',)
    
@admin.register(paciente)
class BitokuAdmin(admin.ModelAdmin):
    list_display = ('id', 'apellido_paterno', 'apellido_materno', 'nombres', 'fecha_nacimiento', 'sexo', 'cedula', 'telefonoPaciente', 'emailPaciente', 'usuario')
    ordering = ('id',)

@admin.register(especialidad)
class BitokuAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'institucion', 'anio_recebimiento')
    ordering = ('id',)

@admin.register(doctor)
class BitokuAdmin(admin.ModelAdmin):
    list_display = ('id', 'apellido_paterno', 'apellido_materno', 'nombres', 'sexo', 'cedula', 'telefonoDoctor', 'emailDoctor', 'especialidad')
    ordering = ('id',)

@admin.register(citaMedica)
class BitokuAdmin(admin.ModelAdmin):
    list_display = ('id', 'fechaCita', 'horaCita', 'estadoCita', 'paciente', 'doctor')
    ordering = ('id',)