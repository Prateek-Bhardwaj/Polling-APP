from django.contrib import admin
from .models import Poll, User
# Register your models here.
admin.site.register(Poll)
admin.site.register(User)