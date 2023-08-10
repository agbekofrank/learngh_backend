
from django.forms import ModelForm
from .models import NoteInstance


class NoteForm(ModelForm):

    # def clean_title(self):
    #     data = self.cleaned_data['title']
    #     if not data.is_valid:
    #         raise ValidationError(_("Titles must be unique"))

    class Meta:
        model = NoteInstance
        fields = ['title', 'body', 'created', 'updated']
