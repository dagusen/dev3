# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.contrib.auth import get_user_model

from django.http import Http404

from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import render, get_object_or_404, redirect

from django.views.generic import DetailView, View, ListView

from partylists.models import PartyList

from positions.models import Position

from .models import Candidate

User = get_user_model()

# Create your views here.

class CandidateVoteToggle(View):
	def post(self, request, *args, **kwargs):
		username_to_toggle = request.POST.get("username")
		candidate_, is_voted = Candidate.objects.toggle_vote(request.user, username_to_toggle)
		return redirect('/candidate/%s' % candidate_.user.username )

class CandidateDetailView(LoginRequiredMixin, DetailView):
	template_name = 'candidates/user.html'

	def get_object(self):
		username = self.kwargs.get("username")
		if username is None:
			raise Http404
		return get_object_or_404(User, username__iexact=username, is_active=True)

	# search
	def get_context_data(self, *args, **kwargs):
		context =super(CandidateDetailView, self).get_context_data(*args, **kwargs)
		user = context['user']

		#form toggle
		is_voted = False
		if user.candidate in self.request.user.is_voted.all():
		 	is_voted = True
		context['is_voted'] = is_voted

		query = self.request.GET.get('q')
		Position_exists = Position.objects.filter(user=user).exists()
		qs = PartyList.objects.filter(owner=user).search(query)
		if Position_exists and qs.exists():
			context['partylist'] = qs
		return context