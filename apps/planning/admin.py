from django.contrib import admin

from apps.planning.models import Tenantry, Schedule, RentHours


@admin.register(Tenantry)
class TenantryAdmin(admin.ModelAdmin):
	fields = ['name', 'phone']
	list_display = ['name', 'phone']
	search_fields = ['name', 'phone']


@admin.register(RentHours)
class RentHourAdmin(admin.ModelAdmin):
	fields = ['day', 'time']
	list_display = ['day', 'time']


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
	fields = ['tenantry', 'schedule_hours']
	list_display = ['tenantry']
	search_fields = ['tenantry__name', 'tenantry__phone']