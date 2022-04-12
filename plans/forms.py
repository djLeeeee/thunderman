from django import forms
from .models import Plan


class PlanForm(forms.ModelForm):
    # 전체적으로 보기 좋게 하기 위해 넓이는 form의 길이에 맞춘다.
    box_class = 'w-100 my-2'
    large_box_class = 'w-100 my-2'

    title = forms.CharField(
        max_length=20,
        widget= forms.TextInput(
            attrs={
                'class': box_class
                
            }
        )
    )

    date = forms.DateField(
        widget= forms.DateInput(
            attrs={
                'class': box_class,
                'type': 'date',
            }
        )
    )

    time = forms.TimeField(
        widget= forms.TimeInput(
            attrs={
                'class': box_class,
                'type': 'time',
                # step은 30분 단위로 설정
                'step': '1800',
            }
        )
    )

    people_limit = forms.IntegerField(
        widget= forms.NumberInput(
            attrs={
                'placeholder': '몇 명?',
                'min': 0,
                'max': 10,
                'class': box_class,
            }
        )
    )

    place = forms.CharField(
        max_length=20,
        widget= forms.TextInput(
            attrs={
                'class': box_class,
            }
        )
    )

    description = forms.CharField(
        widget= forms.Textarea(
            attrs={
                'placeholder': '어떤 모임인지 자세히 작성해 주세요.',
                'cols': 40,
                'rows': 10,
                'class': large_box_class,
            }
        )       
    )
    


    class Meta:
        model = Plan
        fields = '__all__'
