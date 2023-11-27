from django.contrib import admin
from django.contrib.contenttypes.admin import GenericStackedInline
from django.contrib.auth.models import User

from .models import *

class Choices(admin.TabularInline):
    model = Choice
    fields = ['choice']
    extra = 1

class Comments(GenericStackedInline):
    model = Comment
    fields = ['comment']
    extra = 1


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question"]}),
    ]
    inlines = [Choices, Comments]

    list_display = ["question", "pub_date", "last_edit"]


admin.site.register(Question, QuestionAdmin)

