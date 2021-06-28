from django import forms
from django.contrib.auth.models import User

from .models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title','description','complete']

        widgets = {
            'title': forms.TextInput(attrs = {'id':'title-id'}),
            'description': forms.Textarea(attrs = {'id': 'description-id', 'rows': 5}),
            'complete': forms.CheckboxInput(attrs = {'id': 'complete-id'})
        }