from django.contrib import admin
from .models import Account
# Register your models here.
from django.contrib.auth.admin import UserAdmin


class AccountAdmin(UserAdmin):
    list_display = ('email', 'username', 'first_name', 'last_name', 'last_login', 'is_active', 'date_joined')
    list_display_links = ('email', 'first_name', 'last_name')
    search_fields = ()
    readonly_fields = ('last_login', 'date_joined')
    ordering = ('-date_joined',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Account, AccountAdmin)