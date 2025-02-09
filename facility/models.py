from django.db import models
from simple_history.models import HistoricalRecords
from facility_mgn.abstract_models import TimeStampedModel
from django.db.models.query_utils import Q
from facility_mgn.utils import genserial
from django.urls import reverse

# Create your models here.
REPOT_STATUS_CHOICE = (
    ("pending", "Pending"),
    ("assigned", "Assigned"),
    ("treated", "Treated"),
    ("rejected", "Rejected"),
)

class Report(TimeStampedModel):
    """ A model to track user's report on any faulty facility/equipment within the faculty."""
    tracking_number = models.CharField(max_length=10, default=genserial)
    actor = models.ForeignKey(
        "accounts.User", on_delete=models.PROTECT, limit_choices_to=Q(user_type="student"),
        related_name="faulty_reports"
    )
    subject = models.CharField(max_length=50)
    department = models.ForeignKey(
        "accounts.Department", on_delete=models.PROTECT, limit_choices_to=Q(status="active")
    )
    photo = models.ImageField(blank=True, null=True, upload_to="faulty_report")
    note = models.TextField()
    status = models.CharField(
        max_length=50, choices=REPOT_STATUS_CHOICE, default="pending")
    technician = models.ForeignKey(
        "accounts.User", on_delete=models.PROTECT, limit_choices_to=Q(user_type="technician"),
        related_name="tasks",
        blank=True, null=True,
    )
    history = HistoricalRecords(bases=[TimeStampedModel])

    class Meta:
        verbose_name = "Faulty Report"
        verbose_name_plural = "Faulty Reports"
        ordering = ("-updated", )

    def audits(self):
        dta = self.history.all().order_by('-history_date')[:2].values()
        return dta

    def revisions(self):
        "Count of how many changes were made to this instance"
        return self.history.count()

    def get_absolute_url(self):
        return reverse("facility:report-details", kwargs={"uid": self.tracking_number})

    def get_update_url(self):
        return reverse("facility:report-update", kwargs={"uid": self.tracking_number})
    
    def __str__(self) -> str:
        return f"{self.subject}"


class FacilityInventory(TimeStampedModel):
    """ A model to track facility Inventory"""
    tracking_number = models.CharField(max_length=10, default=genserial)
    name = models.CharField(max_length=100, )
    image = models.ImageField(upload_to="uploads/facility/inventory", blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    quantity = models.PositiveBigIntegerField(default=0)

    class Meta:
        verbose_name = "Facility Inventory"
        verbose_name_plural = "Facilities Inventory"
        ordering = ("-updated", )


    def __str__(self) -> str:
        return f"{self.name}"
