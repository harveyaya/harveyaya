from django.conf.urls import url

from views import (
    diaryHomeView,
)

urlpatterns = [
    url(r'^$', diaryHomeView.as_view(), name = "diary_name"),
]