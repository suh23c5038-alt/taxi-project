from django.contrib import admin
from .models import Station, Route

# تسجيل نموذج المحطة لظهوره في لوحة التحكم
admin.site.register(Station)

# تسجيل نموذج المسار لظهوره في لوحة التحكم
admin.site.register(Route)