import datetime
from django import forms
from .models import Plan, Comment


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
                'value' : datetime.date.today(),
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
                'value' : '19:00:00',
            }
        )
    )

    people_limit = forms.IntegerField(
        widget= forms.NumberInput(
            attrs={
                'placeholder': '제한이 없을시 0을 입력해주세요',
                'min': 0,
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
        exclude = ('user', 'join_users',)


class CommentForm(forms.ModelForm):
    large_box_class = 'w-100 my-2'
    content = forms.CharField(
        widget= forms.Textarea(
            attrs={
                'placeholder': '로그인 후 댓글을 작성해주세요',
                'cols': 10,
                'rows': 4,
                'class': large_box_class,
            }
        )       
    )

    class Meta:
        model = Comment
        fields = ('content',)