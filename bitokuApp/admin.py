from django.contrib import admin
from .models import usuario, paciente, especialidad, doctor
# Register your models here.

admin.site.register(usuario)
admin.site.register(paciente)
admin.site.register(especialidad)
admin.site.register(doctor)