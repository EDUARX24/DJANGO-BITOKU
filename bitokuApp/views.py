import json
from django.shortcuts import render
from django.contrib.auth.models import User
from .utils import validate_fields

def home(request):
    return render(request, 'home.html')

def login(request):
    context = {}
    return render(request, 'auth/login.html', context)

def register(request):
    context = {}

    # Validaciones
    if request.method == 'POST':
        fields = {
            'first_name': request.POST.get('first_name'),
            'last_name': request.POST.get('last_name'),
            'username': request.POST.get('username'),
            'email': request.POST.get('email'),
            'password': request.POST.get('password'),
            'password2': request.POST.get('password2'),
        }

        # Validar campos vacíos
        redirect_url = 'register'
        validation_error = validate_fields(fields, redirect_url)
        if validation_error:
            return render(request, 'auth/register.html', {'data': json.dumps(validation_error)})

        # Continuar con la lógica de registro si no hay errores de validación
        if fields['password'] == fields['password2']:
            if User.objects.filter(username=fields['username']).exists():
                context = {
                    'data': json.dumps({
                        'icon': 'error',
                        'title': 'Error',
                        'text': 'El usuario ya existe - No disponible',
                        'redirect': redirect_url
                    })
                }
            else:
                if User.objects.filter(email=fields['email']).exists():
                    context = {
                        'data': json.dumps({
                            'icon': 'error',
                            'title': 'Error',
                            'text': 'El email ya existe',
                            'redirect': redirect_url
                        })
                    }
                else:
                    user = User.objects.create_user(
                        username=fields['username'],
                        password=fields['password'],
                        email=fields['email'],
                        first_name=fields['first_name'],
                        last_name=fields['last_name']
                    )
                    user.save()
                    context= {
                        'data': json.dumps({
                            'icon': 'success',
                            'title': 'Usuario creado',
                            'text': 'El usuario se ha creado correctamente',
                            'redirect': 'login'
                        })
                    }
        else:
            context = {
                'data': json.dumps({
                    'icon': 'error',
                    'title': 'Error',
                    'text': 'Las contraseñas no coinciden',
                    'redirect': redirect_url
                })
            }

    return render(request, 'auth/register.html', context)
