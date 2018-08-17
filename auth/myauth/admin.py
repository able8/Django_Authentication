from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import CommonUserForm

# Register your models here.
class CommonUserFormInline(admin.TabularInline):
    model = CommonUserForm
    can_delete = False
    verbose_name_plural = '普通会员表' # 网页显示文字
    # verbose_name_plural = 'CommonUserForm'

class UserAdmin(BaseUserAdmin):
    inlines = (CommonUserFormInline,)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)