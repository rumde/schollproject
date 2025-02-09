from django.db import models
from django.conf import settings

from facility_mgn.abstract_models import TimeStampedModel
from facility_mgn.nigeria_states import NIGERIA_STATES
from django_countries.fields import CountryField
# from django.utils.translation import ugettext_lazy as _
from django.utils.translation import gettext_lazy as _

##
from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser

from .managers import UserManager
##
from django.utils.html import strip_tags
from django.template.loader import render_to_string
from django.utils import timezone
from django.contrib.auth.tokens import default_token_generator
from simple_history.models import HistoricalRecords
from facility_mgn.utils import genserial

RELIGION_CHOICE = (
    ("islam", "Islam"),
    ("christianity", "Christianity"),
    ("others", "Others"),
)

STATUS_CHOICE = (
    ("active", "Active"),
    ("pending", "Pending"),
    ("blocked", "Blocked"),
    ("inactive", "Inactive"),
)
GENDER_CHOICE = (("male", "Male"), ("female", "Female"), ("others", "Others"))


USER_TYPE_CHOICE = (
    ("student", "Student"),
    ("technician", "Technician"),
    ("staff", "Staff"),
    ("admin", "Admin"), 
    ("super_admin", "Super Admin")
)



class User(AbstractBaseUser, PermissionsMixin, TimeStampedModel):
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=30,)
    other_name = models.CharField(_('other name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    user_type = models.CharField(max_length=255, choices=USER_TYPE_CHOICE, default="student")
    gender = models.CharField(
        max_length=15, choices=GENDER_CHOICE, default="others")
    phone_number=models.CharField(max_length = 15, blank = True, null = True,)
    image = models.ImageField(upload_to="profile_pics", null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    country = CountryField(multiple=False, null=True, blank=True)
    state = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    department = models.ForeignKey("accounts.Department", blank=True, null=True,
                               on_delete=models.SET_NULL , related_name="staffs")
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_(
            'Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(_('active'), default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name"]

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        ordering = ("-updated", )

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = f"{self.first_name} {self.other_name} {self.last_name}"
        return full_name.strip()

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Sends an email to this User.
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs)

    @property
    def country_title(self):
        if self.country:
            return self.country.name


    def __str__(self):
        return self.email


class Department(TimeStampedModel):
    uid = models.CharField(max_length=10, default=genserial)
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(
        upload_to="department/images", blank=True, null=True)
    address = models.TextField()
    state = models.CharField(max_length=50, choices=NIGERIA_STATES)
    status = models.CharField(
        max_length=50, choices=STATUS_CHOICE, default="pending")
    history = HistoricalRecords(bases=[TimeStampedModel])

    class Meta:
        verbose_name = "Department"
        verbose_name_plural = "Departments"
        ordering = ("-updated", )

    def audits(self):
        dta = self.history.all().order_by('-history_date')[:2].values()
        return dta

    def revisions(self):
        "Count of how many changes were made to this instance"
        return self.history.count()

    def __str__(self) -> str:
        return f"{self.title}"
