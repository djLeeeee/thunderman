from django.urls import path
from . import views

app_name = "plans"

urlpatterns = [
    # main - 전체 페이지 조회
    path("", views.index, name="index"),
    # 해당 날짜의 전체 약속 조회
    path("<int:date>/", views.plan_date, name="plan_date"),
    # 해당 약속 조회
    path("<int:pk>/detail/", views.plan_detail, name="plan_detail"),
    # 약속 추가
    path("create/", views.plan_create, name="plan_create"),
]
