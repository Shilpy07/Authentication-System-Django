from django.contrib import admin
from Learnings.models import Login


# Register your models here.
class LoginAdmin(admin.ModelAdmin):
    list_display = ('Username', 'Password')
    search_fields = ('Username', 'Password')


admin.site.register(Login, LoginAdmin)
