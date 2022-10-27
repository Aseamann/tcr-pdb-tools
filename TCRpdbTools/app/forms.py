from django import forms

from martor.fields import MartorFormField
from app.models import Post, FUNCTION_CHOICES


class SimpleForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput())
    description = MartorFormField()
    wiki = MartorFormField()


class PdbToolsForm(forms.Form):
    pdb = forms.CharField(widget=forms.TextInput())
    action1 = forms.CharField(
        max_length=50,
        widget=forms.Select(choices=FUNCTION_CHOICES),
    )
    action1 = forms.CharField(
        max_length=50,
        widget=forms.Select(choices=FUNCTION_CHOICES),
    )
    action1 = forms.CharField(
        max_length=50,
        widget=forms.Select(choices=FUNCTION_CHOICES),
    )


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"
