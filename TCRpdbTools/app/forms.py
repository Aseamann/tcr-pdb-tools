from django import forms

from martor.fields import MartorFormField
from app.models import PdbToolsForm, FUNCTION_CHOICES, PDB_CHOICES


class PdbToolsForm(forms.Form):
    pdb = forms.CharField(
        max_length=4,
        widget=forms.Select(choices=PDB_CHOICES),
    )
    action1 = forms.CharField(
        max_length=50,
        widget=forms.Select(choices=FUNCTION_CHOICES),
    )
    action2 = forms.CharField(
        max_length=50,
        widget=forms.Select(choices=FUNCTION_CHOICES),
    )
    action3 = forms.CharField(
        max_length=50,
        widget=forms.Select(choices=FUNCTION_CHOICES),
    )


class PostPdbForm(forms.ModelForm):
    class Meta:
        mode = PdbToolsForm
        fields = "__all__"
        widgets = {
            'pdb': forms.Select(attrs={'class': 'form-control'}),
            'action1': forms.Select(attrs={'class': 'form-control'}),
            'action2': forms.Select(attrs={'class': 'form-control'}),
            'action3': forms.Select(attrs={'class': 'form-control'}),
        }
