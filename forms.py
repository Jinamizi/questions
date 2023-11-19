from django import forms

class MailForm(forms.Form):
    subject = forms.CharField(min_length=3, max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)