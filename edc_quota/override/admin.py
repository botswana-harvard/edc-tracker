from django.contrib import admin

from .models import OverrideModel


class OverrideAdmin(admin.ModelAdmin):
    fields = ('request_code', 'override_code', )
admin.site.register(OverrideModel, OverrideAdmin)
