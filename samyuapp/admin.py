from django.contrib import admin

from samyuapp.models import Praveen


class PraveenAdmin(admin.ModelAdmin):
    pass


admin.site.register(Praveen, PraveenAdmin)

