from django.contrib import admin
from .models import Management
import django.contrib.auth.admin
import django.contrib.auth.models
from django.contrib import auth


admin.site.unregister(auth.models.Group)

admin.site.register(Management)
admin.site.site_header = 'DIU-Graduate Management System' 
