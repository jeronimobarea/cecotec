from django.contrib import admin

from cecotec.apps.user.models import User


# Register your models here.
class CustomUserAdmin(admin.ModelAdmin):
    readonly_fields = ['id', 'last_login', 'password', 'created_at', 'last_modification', ]
    search_fields = ['email', ]
    date_hierarchy = 'last_login'
    list_filter = ('is_active', 'is_staff', 'is_superuser',)

    fieldsets = (
        ('Register data', {'fields': ('id', 'email', 'password')}),
        ('Status', {'fields': ('is_active', 'is_staff', 'is_superuser',)}),
        ('Time control', {'fields': (('last_login', 'last_modification', 'created_at',),)}),
        ('Permissions', {'fields': ('groups', 'user_permissions')}),
    )
    filter_horizontal = ('groups', 'user_permissions',)


admin.site.register(User, CustomUserAdmin)
