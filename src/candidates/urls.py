from django.conf.urls import url

from .views import (
    CandidateDetailView
)

urlpatterns = [
    url(r'^(?P<username>[\w-]+)/$', CandidateDetailView.as_view(), name='detail'),
]