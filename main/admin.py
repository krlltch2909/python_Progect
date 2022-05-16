from django.contrib.auth.admin import UserAdmin

from django.contrib import admin
from .models import AccauntUser
from .form import AccauntUserCreationForm, AccauntUserChangeForm

# Register your models here.


admin.site.register(AccauntUser)


class CustomUserAdmin(UserAdmin):
    model = AccauntUser
    add_form = AccauntUserCreationForm

    # add_fieldsets = (
    #     *UserAdmin.add_fieldsets, (
    #         'CustomFields', {
    #             'fields': (
    #                 'login'
    #                 'password'
    #             )
    #         }
    #     )
    # )
    #
    # fieldsets = (
    #     *UserAdmin.fieldsets, (
    #         'CustomFields', {
    #             'fields': (
    #                 'login'
    #                 'password'
    #             )
    #         }
    #     )
    # )
