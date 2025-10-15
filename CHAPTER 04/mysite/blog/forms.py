from django import forms
from blog import models


class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=255)
    email = forms.EmailField(max_length=255)
    to = forms.EmailField(max_length=255)
    comments = forms.CharField(required=False, widget=forms.Textarea)


class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ["name", "email", "body"]
