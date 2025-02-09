from django import forms
from .models import Report
from facility_mgn.widgets import ImageWidget

class SubmitReportForm(forms.ModelForm):
    class Meta:
        model = Report
        exclude = ("tracking_number", "actor", "status", "technician")
        widgets = {
            "photo": ImageWidget(),
            # "note": Textarea(attrs={"cols": 10, "rows": 3}),
        }


class ReportFormTechnicianUpdate(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ReportFormTechnicianUpdate, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        # if instance and instance.pk:
        self.fields['tracking_number'].widget.attrs['readonly'] = True
        self.fields['subject'].widget.attrs['readonly'] = True
        self.fields['actor'].widget.attrs['readonly'] = True
        self.fields['department'].widget.attrs['readonly'] = True
        self.fields['note'].widget.attrs['readonly'] = True
        # self.fields['technician'].widget.attrs['readonly'] = True
    class Meta:
        model = Report
        exclude = ("technician",)
        widgets = {
            "photo": ImageWidget(),
            # "note": Textarea(attrs={"cols": 10, "rows": 3}),
        }

    def clean_tracking_number(self):
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            return instance.tracking_number
        else:
            return self.cleaned_data['tracking_number']

    def clean_subject(self):
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            return instance.subject
        else:
            return self.cleaned_data['subject']

    def clean_actor(self):
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            return instance.actor
        else:
            return self.cleaned_data['actor']

    def clean_department(self):
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            return instance.department
        else:
            return self.cleaned_data['department']

    def clean_note(self):
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            return instance.note
        else:
            return self.cleaned_data['note']
