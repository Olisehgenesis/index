from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Paper)
admin.site.register(Objective)
admin.site.register(User)
admin.site.register(structured)