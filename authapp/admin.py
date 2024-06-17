from django.contrib import admin
from authapp.models import Contacto,Membresia,Entrenadore,Usuario,Asistencia
# Register your models here.
admin.site.register(Contacto)
admin.site.register(Membresia)
admin.site.register(Usuario)
admin.site.register(Entrenadore)
admin.site.register(Asistencia)

