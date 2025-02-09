from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

from .models import Report, FacilityInventory
# Register your models here.


@admin.register(Report)
class ReportAdmin(SimpleHistoryAdmin):
    list_display = (
        "tracking_number",
        "actor",
        "subject",
        "department",
        "technician",
        "status",
        "timestamp",
        "updated",
    )
    list_filter = ("status", "timestamp", "updated", )
    readonly_fields = ("tracking_number",)


@admin.register(FacilityInventory)
class FacilityInventoryAdmin(SimpleHistoryAdmin):
    list_display = (
        "tracking_number",
        "name",
        "quantity",
        "timestamp",
        "updated",
    )
    list_filter = ("timestamp", "updated", )
    readonly_fields = ("tracking_number",)
