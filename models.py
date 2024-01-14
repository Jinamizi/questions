from django.db import models
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.utils.translation import gettext, gettext_lazy as _

#TODO add user login
#TODO add polls
#TODO add hints
#TODO add feedback using mail
#FIXME move to GenericForeignKey later
#FIXME use django authentication 
#FIXME use a base class for Question and Comment: https://www.youtube.com/shorts/wNjtGky2nys
#FIXME if user deletes account, ask if he wants to delete question. use on_delete=models.SET_NULL, and set null=True


class Question(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='questions') 
    question = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True, editable=False)
    last_edit = models.DateTimeField(auto_now=True, editable=False)

    #comment = GenericRelation('Comment', related_query_name='comment')
    reaction = GenericRelation('Reaction', related_query_name='reactions')

    class Meta:
        ordering = ["-pub_date"]
        verbose_name = "question"
        verbose_name_plural = "questions"
        db_table = "Questions"

    def __str__(self):
        return self.question

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
    choice = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)
    pub_date = models.DateTimeField(auto_now_add=True)
    last_edit = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "Choices"

    def __str__(self):
        return self.choice

#COMPLETE add ability to add comments to comments
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments') #person who commented
    question = models.ForeignKey(Question, on_delete= models.CASCADE, related_name='comments')
    comment = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True, editable=False)
    last_edit = models.DateTimeField(auto_now=True, editable=False)

    reaction = GenericRelation('Reaction', related_query_name='comment')
    # child_comment = GenericRelation('self', related_query_name='child_comments') 

    # # Self-referential relationship for comments on comments
    # #parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, related_name='child_comments', null=True, blank=True)

    # content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    # object_id = models.PositiveIntegerField()
    # content_object = GenericForeignKey()

    class Meta:
        ordering = ["-pub_date"]
        db_table = "Comments"

    def __str__(self):
        return self.comment
    
class Reaction(models.Model):
    LIKE = 'LIKE'
    DISLIKE = 'DISLIKE'
    REACTION_CHOICES = (
        (LIKE, 'Like'),
        (DISLIKE, 'Dislike'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE) #the user reacting
    reaction = models.CharField(max_length=10, choices=REACTION_CHOICES)
    time = models.DateTimeField(auto_now=True, editable=False)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE) #foreign key to either a comment or a question
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()

    class Meta:
        unique_together = ('user', 'content_type')  # To ensure a user can react to a post only once
        db_table = "Reactions"


    def __str__(self):
        return self.reaction