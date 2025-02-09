from django.urls import path
from .views import (
    SubmitReportView,
    ReportListView,
    ReportDetailsView,
    ReportUpdateView,
) 
urlpatterns = [
    path("report/add/", SubmitReportView.as_view(), name="report-add"),
    path("report/list/", ReportListView.as_view(), name="report-list"),
    path("report/details/<uid>/", ReportDetailsView.as_view(), name="report-details"),
    path("report/update/<uid>/", ReportUpdateView.as_view(), name="report-update"),
]
