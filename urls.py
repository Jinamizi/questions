from django.urls import path

from . import views

app_name = "example"
urlpatterns = [
    path('questions', views.QuestionsList.as_view(), name='questions' ),
]
