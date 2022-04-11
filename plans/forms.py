from django import forms
from .models import Plan


class PlanForm(forms.ModelForm):

    title = forms.CharField(
        max_length=20,
        widget= forms.TextInput(
        )
    )

    date = forms.DateField(
        widget= forms.DateInput(
            attrs={
                'type': 'date',
            }
        )
    )

    time = forms.TimeField(
        widget= forms.TimeInput(
            attrs={
                'type': 'time',
            }
        )
    )

    people_limit = forms.IntegerField(
        widget= forms.NumberInput(

        )
    )

    place = forms.CharField(
        max_length=20,
        widget= forms.TextInput(
        )
    )

    description = forms.Textarea()


    class Meta:
        model = Plan
        fields = '__all__'
