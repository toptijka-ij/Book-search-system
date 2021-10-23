from django.contrib import admin

from .models import CustomUser

# class CustomUserAdmin(admin.ModelAdmin):
#     list_display = ('date_joined',)
#     search_fields = ('username', 'email', 'first_name', 'last_name')
#     fields = (('username', 'email'), ('first_name', 'last_name'), ('send—messages', 'is_active'),
#               ('is_staff', 'is_superuser'), 'groups', 'user_permissions', ('last—login', 'date_joined'))
#     readonly_fields = ('last_login', 'date_joined')


admin.site.register(CustomUser)
