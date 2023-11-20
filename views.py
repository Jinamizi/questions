from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from django.core.mail import send_mail

from .forms import MailForm


