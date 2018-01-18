from django.conf.urls import url

from views import (
    EnterPageView,
    HomePageView,
)

urlpatterns = [
    url(r'^$', EnterPageView.as_view(), name="enter_page"),
    url(r'^home/$', HomePageView.as_view(), name="external_homepage"),
]