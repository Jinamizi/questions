from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.views.generic.list import ListView

from .models import *

class QuestionsList(ListView):
    model = Question


