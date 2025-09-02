from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("xabarlar/", views.message_list, name="message_list"),
]
