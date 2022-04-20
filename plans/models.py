from django.db import models
from django.conf import settings
from datetime import date

# Create your models here.

class Plan(models.Model):

    # user 정보
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # 약속 제목
    title = models.CharField(max_length=20)

    # 약속 날짜
    date = models.DateField()

    # 약속 시간
    time = models.TimeField()

    # 약속 최대 인원
    people_limit = models.IntegerField() 

    # 약속 장소
    place = models.CharField(max_length=20)

    # 약속 설명
    description = models.TextField()

    # 약속 생성 시간
    created_at = models.DateTimeField(auto_now_add=True)

    # 참가 명단
    join_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='join_plans')

    def __str__(self) -> str:
        return super().__str__()


class Comment(models.Model):
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content