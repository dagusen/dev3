from django.conf.urls import url

from .views import (
    CandidateDetailView,
    CandidateListView,
    CandidateCreateView
)

urlpatterns = [
	url(r'^$', CandidateListView.as_view(), name='list'),
	url(r'^create/$', CandidateCreateView.as_view(), name='create'),
    url(r'^(?P<username>[\w-]+)/$', CandidateDetailView.as_view(), name='detail'),
]