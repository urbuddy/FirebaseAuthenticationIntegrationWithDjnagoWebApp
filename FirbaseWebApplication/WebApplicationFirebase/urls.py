from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("signup/", views.signup, name="signup"),
    path("signin/", views.signin, name="signin"),
    path("reset_password/", views.reset_password, name="reset_password"),
    path("profile/", views.profile, name="profile"),
    path("logout/", views.logout, name="logout")
]
