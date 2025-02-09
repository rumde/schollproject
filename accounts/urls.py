from django.urls import path
from .views import (
    HomeView,
    UserSignupView,
    UserLoginView,
    DashboardView,
    StudentDashboardView,
    TechnicianDashboardView,
)
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("logout/", LogoutView.as_view(), {"next_page": "/"}, name="logout"),
    path("register/", UserSignupView.as_view(), name="signup"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("dashboard/", DashboardView.as_view(), name="dashboard"),
    path(
        "dashboard/student/", StudentDashboardView.as_view(), name="student-dashboard"
    ),
    path(
        "dashboard/technician/", TechnicianDashboardView.as_view(), name="technician-dashboard"
    ),
    path("", HomeView.as_view()),
    # path("", UserLoginView.as_view()),
]
