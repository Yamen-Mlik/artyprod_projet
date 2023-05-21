from django.contrib import admin
from .models import Task
admin.site.register(Task)
from .models import Personnel
admin.site.register(Personnel)
from .models import Projet
admin.site.register(Projet)
from .models import Service
admin.site.register(Service)
from .models import Detail
admin.site.register(Detail)
from .models import Equipe
admin.site.register(Equipe)
from .models import Profile
admin.site.register(Profile)


# Register your models here.
