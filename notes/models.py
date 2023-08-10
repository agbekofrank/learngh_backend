from django.db import models

# Create your models here.


class NoteInstance(models.Model):
    title = models.CharField(
        unique=True, max_length=300, blank=False, null=True)
    body = models.TextField(blank=False, null=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self) -> str:
        return self.title
