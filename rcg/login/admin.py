from django.contrib import admin
from .models import new_user
from .models import Member


# Register your models here.
admin.site.register(new_user)
admin.site.register(Member)
