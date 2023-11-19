from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from django.core.mail import send_mail

from .forms import MailForm

#TODO jdfkajdfa
#FIXME fix this
def get_name(request):
    if request.method == "POST":
        form = MailForm(request.POST)
        if form.is_valid():
            
            return render(request, 'example/test.html', {"data": form.cleaned_data})
    else:
        form = MailForm()

    return render(request, 'example/name.html', {"form": form})
