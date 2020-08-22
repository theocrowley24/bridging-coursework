from django.contrib import admin
from .models import Cv
from .models import Qualification
from .models import Experience

admin.site.register(Cv)
admin.site.register(Qualification)
admin.site.register(Experience)
