from django.contrib import admin
from .models import (
    User,
    Vehicle,
    Drive,
)

admin.site.register(User)
admin.site.register(Vehicle)
admin.site.register(Drive)