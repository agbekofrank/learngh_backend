from django.db.models import Model, CharField, EmailField, DateTimeField, TextField

# Create your models here.

class UserInstance(Model):
    
    name = CharField(max_length=300, blank=False, null=True)
    username = CharField(max_length=300, blank=False, null=True)
    email = EmailField(null=True)
    phone = CharField(unique=True, max_length=20, blank=True, null=True)
    # phone = CharField(unique=True, max_length=20, blank=True, null=True)

    # address, 

    def __str__(self) -> str:
        return self.name
    


class NoteInstance(Model):
    title = CharField(
        unique=True, max_length=300, blank=False, null=True)
    body = TextField(blank=False, null=True)
    created = DateTimeField(auto_now_add=True, auto_now=False)
    updated = DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self) -> str:
        return self.title