from django.db import models
from .choises import sexos
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='users/usuario_defecto.jpg', upload_to='profile_pics/', verbose_name='Imagen de perfil')
    sexo = models.CharField(max_length=1, choices=sexos, default='M')
    telefono = models.CharField(max_length=10, blank=True, null=True)
    cedula = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'
        db_table = 'Perfil'
        ordering = ['-id']

    def __str__(self):
        return f'{self.user.username} Profile'
    
def create_user_profile(sender, instance, created ,**kwargs): 
    if created:
        Profile.objects.create(user=instance)

def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)

#   METODOS DE LAS NUEVAS TABLAS
class paciente(models.Model):
    fecha_nacimiento = models.DateField(verbose_name="Fecha de Nacimiento")
    #Relacion con la tabla usuario
    usuario = models.ForeignKey(Profile,null=True, blank=True, on_delete=models.CASCADE)

    def nombre_completo(self):
        return self.fecha_nacimiento.strftime('%d/%m/%Y')
    
    def __str__(self):
        return self.nombre_completo()
    
    class Meta:
        verbose_name = "Paciente"
        verbose_name_plural = "Pacientes"
        db_table = "paciente"


class especialidad(models.Model):
    nombre = models.CharField(max_length=30,default='Sin Especialidad', verbose_name="Nombre de la Especialidad")
    institucion = models.CharField(max_length=30, verbose_name="Institución")
    anio_recebimiento = models.DateField(verbose_name="Año de Recebimiento")

    def nombre_especialidad(self):
        return self.nombre + " " + self.institucion 
        
    def __str__(self):
        return self.nombre_especialidad()

    class Meta:
        verbose_name = "Especialidad"
        verbose_name_plural = "Especialidades"
        db_table = "especialidad"

class doctor(models.Model):
    apellido_paterno =  models.CharField(max_length=20, verbose_name="Apellido Paterno")
    apellido_materno = models.CharField(max_length=20, verbose_name="Apellido Materno")
    nombres = models.CharField(max_length=20, verbose_name="Nombres")
    telefonoDoctor = models.IntegerField(verbose_name="Teléfono")
    emailDoctor = models.CharField(max_length=50, verbose_name="Email")
    cedula = models.CharField(max_length=60, verbose_name="Cédula")
    sexo = models.CharField(max_length=1, choices=sexos, default='M', verbose_name="Sexo")
    cedula = models.CharField(max_length=50, verbose_name="Cédula")
    
    #Relacion table Doctor -> Usuario & Doctor -> Especialidad
    usuario =  models.ForeignKey(Profile, null=True, blank=True, on_delete=models.CASCADE)
    especialidad = models.ForeignKey(especialidad, null=True, blank=True, on_delete=models.CASCADE)  

    def nombre_completo(self):
        return self.apellido_paterno + " " + self.apellido_materno + " " + self.nombres
    
    def __str__(self):
        return self.nombre_completo()
    
    class Meta:
        verbose_name = "Doctor"
        verbose_name_plural = "Doctores"
        db_table = "doctor"
        ordering = ['apellido_paterno', '-apellido_materno']

class citaMedica(models.Model):
    fechaCita = models.DateField(verbose_name="Fecha de la Cita")
    horaCita = models.TimeField(verbose_name="Hora de la Cita")
    estadoCita = models.IntegerField(default=1,verbose_name="Estado de la Cita")
    motivoCancelacion = models.CharField(max_length=240,null=True,blank=True, verbose_name="Motivo de Cancelación")

    #Relacion table paciente -> citaMedica & doctor -> citaMedica
    paciente = models.ForeignKey(paciente, null=True, blank=True, on_delete=models.CASCADE)
    doctor = models.ForeignKey(doctor, null=True, blank=True, on_delete=models.CASCADE)

    def serializarTabla(self):
        return self.fechaCita.strftime('%d/%m/%Y') + " " + self.horaCita.strftime('%H:%M')

    def __str__(self):
        return self.serializarTabla()

    class Meta:
        verbose_name = "Cita Médica"
        verbose_name_plural = "Citas Médicas"
        db_table = "citaMedica"
        ordering = ['fechaCita', '-horaCita', '-estadoCita']