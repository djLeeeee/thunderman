from django.db import models
from django.conf import settings

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

    def __str__(self) -> str:
        return super().__str__()
