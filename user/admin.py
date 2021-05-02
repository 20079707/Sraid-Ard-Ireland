from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from user.models import User, Staff, NonStaff


class AccountAdmin(UserAdmin):  # user accounts class
    list_display = ('email', 'username', 'first_name', 'date_joined', 'last_login', 'is_admin', 'is_staff')
    readonly_fields = ('date_joined', 'last_login')  # fields cannot be changed
    search_fields = ('email', 'username',)  # search by email or username
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


#
admin.site.register(User, AccountAdmin)  # view user on the admin page
admin.site.register(Staff)  # view staff user on the admin page
admin.site.register(NonStaff)   # view non-staff user on the admin page
