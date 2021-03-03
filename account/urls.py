from django.urls import path

from account import views as account_views


urlpatterns = [
    path("", account_views.register, name="register"),
    path("profile/", account_views.profile, name="profile") 
    ]
