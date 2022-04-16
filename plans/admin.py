from django.contrib import admin
from .models import Plan

class PlanAdmin(admin.ModelAdmin):
    pass


admin.site.register(Plan, PlanAdmin)
