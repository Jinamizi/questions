from django.urls import path

from . import views

app_name = "example"
urlpatterns = [
    path("name/", views.get_name, name="name"),
]
