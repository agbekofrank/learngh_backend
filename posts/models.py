from django.db import models
from users.models import UserInstance

# Create your models here.
class PostInstance(models.Model):

    title = models.CharField(blank=False, max_length=200)
    body = models.TextField(blank=False)
    posted = models.DateTimeField(auto_now_add=True)
    timestamp = models.DateTimeField(auto_now=True)

    tutor = models.ForeignKey(UserInstance,null=True, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title