from django.conf.urls import url, include
from django.views.generic.base import RedirectView

urlpatterns = [
    # --- Product Urls --- #
    url(r'^dear_diary/', include('apps.dear_diary.urls', namespace='dear_diary')),
]
