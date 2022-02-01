from django.contrib import admin
from .models import User, UserGroup, Permission


# Register your models here.
admin.site.register([User, UserGroup, Permission])