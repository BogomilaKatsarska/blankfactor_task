from django.contrib import admin

from bf_task.compute.models import UserCSVProvidedFile, ComputedCSVCalculation


@admin.register(UserCSVProvidedFile)
class UserCSVProvidedFileAdmin(admin.ModelAdmin):
    pass


@admin.register(ComputedCSVCalculation)
class ComputedCSVCalculationAdmin(admin.ModelAdmin):
    pass
