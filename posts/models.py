from django.db import models
from users.models import UserInstance

# Create your models here.


class PostInstance(models.Model):

    title = models.CharField(blank=False, max_length=200)
    body = models.TextField(blank=False)
    posted = models.DateTimeField(auto_now_add=True)
    timestamp = models.DateTimeField(auto_now=True)

    tutor = models.ForeignKey(UserInstance, null=True,
                              on_delete=models.CASCADE)
    
    # tags

    def __str__(self) -> str:
        return self.title


class Like(models.Model):

    author = models.ForeignKey(
        UserInstance, related_name='likes', on_delete=models.CASCADE)
    post = models.ForeignKey(
        PostInstance, related_name='likes', on_delete=models.CASCADE)


class Reactions(models.Model):

    thumps_up = models.PositiveIntegerField(null=True, editable=True)
    wow = models.PositiveIntegerField(null=True, editable=True)
    rocket = models.PositiveIntegerField(null=True, editable=True)
    coffee = models.PositiveIntegerField(null=True, editable=True)
    post = models.ForeignKey(
        PostInstance, null=True, on_delete=models.CASCADE)
