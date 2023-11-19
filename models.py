from django.db import models
from django.utils.translation import gettext, gettext_lazy as _

#TODO add user login
#TODO add polls
#TODO add hints
#TODO add feedback using mail
#FIXME use django authentication 

class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)  # Note: In a real-world scenario, use a more secure way to store passwords
    date_joined = models.DateTimeField(_('date joined'),auto_now_add=True, editable=False) 

    class Meta:
        db_name = "users"
        ordering = ["username"]

    def __str__(self):
        return self.username


class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) #FIXME if user deletes account, ask if he wants to delete question
    question = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    last_edit = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-pub_date"]
        verbose_name = "question"
        verbose_name_plural = "questions"
        db_name = "question"

    def __str__(self):
        return self.question

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)
    pub_date = models.DateTimeField(auto_now_add=True)
    last_edit = models.DateTimeField(auto_now=True)

    class Meta:
        db_name = "choice"

    def __str__(self):
        return self.choice

#TODO add ability to add comments to comments
class Comment(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    last_edit = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-pub_date"]