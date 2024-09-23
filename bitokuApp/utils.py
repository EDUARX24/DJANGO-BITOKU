# def validate_fields(fields, redirect):
#     for field_name, value in fields.items():
#         if not value:
#             return {
#                 'icon': 'error',
#                 'title': 'Error',
#                 'text': f'Todos los campos son necesarios',
#                 'redirect': redirect
#             }
#     return None

def validate_fields(fields, redirect):
    for field_name, value in fields.items():
        if not value:
            return {
                'icon': 'error',
                'title': 'Error',
                'text': 'Todos los campos son necesarios',
                'redirect': redirect
            }
    return None
