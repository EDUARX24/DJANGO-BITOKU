from django.contrib.auth.models import Group
from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Profile

@receiver(post_save, sender=Profile)
def add_user_to_rol(sender, instance, created, **kwargs):
    if created and not instance.user.is_superuser:  # Evitar que los superusuarios sean asignados a roles específicos
        try:
            paciente = Group.objects.get(name='Paciente')
        except Group.DoesNotExist:
            paciente = Group.objects.create(name='Paciente')
        
        instance.user.groups.add(paciente)
