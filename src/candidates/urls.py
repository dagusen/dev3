from django.conf.urls import url

from .views import (
    CandidateDetailView,
    CandidateListView
)

urlpatterns = [
	url(r'^$', CandidateListView.as_view(), name='list'),
    url(r'^(?P<username>[\w-]+)/$', CandidateDetailView.as_view(), name='detail'),
]