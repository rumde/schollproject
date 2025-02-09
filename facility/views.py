from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse

from facility.models import Report

from .forms import ReportFormTechnicianUpdate, SubmitReportForm
# Create your views here.


class SubmitReportView(LoginRequiredMixin, View):
    """ Allows submission of Faulty Report by a Student"""
    template_name = "facility/report_add.html"

    def post(self, *args, **kwargs):
        context = {}
        form = SubmitReportForm(self.request.POST, self.request.FILES,)
        if form.is_valid():
            application = form.save(commit=False)
            application.actor = self.request.user
            application.save()
            msg = "Your Faulty Report was successfully submitted!"
            messages.add_message(
                request=self.request,
                level=messages.SUCCESS,
                message=msg,
            )
            return HttpResponseRedirect(reverse("facility:report-list"))
        else:
            msg = "Please correct the error below"
            messages.add_message(
                request=self.request,
                level=messages.ERROR,
                message=msg,
            )
            return render(request=self.request, template_name=self.template_name, context=locals())

    def get(self, *args, **kwargs):
        context = {}
        form = SubmitReportForm()
        context["form"] = form
        return render(request=self.request, template_name=self.template_name, context=context)


class ReportListView(LoginRequiredMixin, View):
    """ Show list of all report by a Student"""
    template_name_student = "facility/report_list_student.html"
    template_name_technician = "facility/report_list_technician.html"
    def get(self, *args, **kwargs):
        user_type = self.request.GET.get("user_type")
        user = self.request.user
        if user_type == "student":
            all_reports = user.faulty_reports.all()
            template_name = self.template_name_student
        elif user_type == "technician":
            all_reports = user.tasks.all()
            template_name = self.template_name_technician
        else:
            all_reports = Report.objects.all()
            template_name = self.template_name_technician
        context = {
            "all_reports": all_reports,
        }
        form = SubmitReportForm()
        context["form"] = form
        return render(request=self.request, template_name=template_name, context=context)


class ReportDetailsView(LoginRequiredMixin, View):
    """ Allows view of Faulty Report by a Student"""
    template_name = "facility/report_details.html"

    def get(self, *args, **kwargs):
        context = {}
        report = get_object_or_404(Report, tracking_number=kwargs.get("uid"))
        form = SubmitReportForm(instance=report)
        context["form"] = form
        return render(request=self.request, template_name=self.template_name, context=context)


class ReportUpdateView(LoginRequiredMixin, View):
    """ Allows update of Faulty Report by a Technician"""
    template_name = "facility/report_update.html"

    def post(self, *args, **kwargs):
        next_url = self.request.POST.get("next_url")
        print(next_url)
        report = get_object_or_404(Report, tracking_number=kwargs.get("uid"))
        form = ReportFormTechnicianUpdate(self.request.POST, self.request.FILES, instance=report)
        if form.is_valid():
            print("valid")
            application = form.save(commit=False)
            # application.last_update_by = profile
            application.save()
            msg = f"Report: {report.tracking_number} Updated Successfully!!!"
            messages.add_message(
                self.request, messages.SUCCESS, message=msg,
            )
            print(msg)
            print(next_url)
            return HttpResponseRedirect(next_url)
        else:
            msg = f"Please Correct the Errors Below!!!"
            messages.add_message(
                self.request, messages.ERROR, message=msg,
            )
            return render(request=self.request, template_name=self.template_name, context=locals())

    def get(self, *args, **kwargs):
        context = {}
        report = get_object_or_404(Report, tracking_number=kwargs.get("uid"))
        form = ReportFormTechnicianUpdate(instance=report)
        context["form"] = form
        return render(request=self.request, template_name=self.template_name, context=context)
