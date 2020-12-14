from django.contrib import admin
from .models import Plan

# Register your models here.


class PlanAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'description',
        'price',
        'image',

    )

    ordering = ('sku',)


admin.site.register(Plan, PlanAdmin)
