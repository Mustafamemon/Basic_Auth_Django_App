from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import User

class NewUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User

class NewUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

class NewUserAdmin(UserAdmin):
    model = User
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {
            'fields': (
                ('is_gp', 'is_os'),
            )
        }
        ),
    )

admin.site.register(User, NewUserAdmin)

admin.site.site_header = "ECOSystem"