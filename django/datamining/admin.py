from django.contrib import admin
from .models import Dota_item_name
from .models import ServisesInSupport
from .models import TableForForm

# Register your models here.

@admin.register(ServisesInSupport)
class ServisesInSupportAdmin(admin.ModelAdmin):
    list_display = ["name", "guid_server", "appearance_time", "ip_adreses", "discription"]


admin.site.register(Dota_item_name)
admin.site.register(TableForForm)



