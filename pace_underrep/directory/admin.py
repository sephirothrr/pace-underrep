from django.apps import apps
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm
import pace_underrep.directory.models as models
from django.utils.translation import gettext, gettext_lazy as _


class DirUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = models.DirUser
        fields = '__all__'


class DirUserAdmin(UserAdmin):
    form = DirUserChangeForm
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    # exclude = ['username',]
    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('first_name', 'last_name', 'email')
    ordering = ['last_name', 'first_name', ]


class DefinitionAdmin(admin.ModelAdmin):
    list_display = ('word', 'definition')
    search_fields = ('word',)


admin.site.register(models.DirUser, DirUserAdmin)
admin.site.register(models.Definition, DefinitionAdmin)
models = apps.get_models()

for model in models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass
