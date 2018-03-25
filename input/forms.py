from django import forms
from .models import Input

class PostForm(forms.ModelForm):

    class Meta:
        model = Input
        fields = ('Course Name', 'Room Preference', 'Class Size', 'Required Equipment', 'Preferred Teaching Time')
