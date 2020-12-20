from django.contrib import admin
from .models import Employees
from .models import Client
from .models import Project
from .models import Post

admin.site.register(Employees)
admin.site.register(Client)
admin.site.register(Project)
admin.site.register(Post)
