from django import forms
from .models import Score


class ScoreForm(forms.ModelForm):

    class Meta:
        model = Score

        fields = [
            "score"
        ]

        widgets = {
            "score": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter score"
                }
            )
        }