from django.contrib import admin
from .models import Role, Team, CustomerUser 

# Register models to appear in Django Admin
admin.site.register(Role)
admin.site.register(Team)
admin.site.register(CustomerUser)
