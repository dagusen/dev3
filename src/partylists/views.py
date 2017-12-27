# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import (
	ListView,
	DetailView,
	CreateView, 
	UpdateView
	)

from .models import PartyList

from .forms import PartyListCreateForm

# Create your views here.

class PartyListListView(LoginRequiredMixin, ListView):
	def get_queryset(self):
		return PartyList.objects.filter(owner=self.request.user)

class PartyListDetailView(LoginRequiredMixin, DetailView):
	def get_queryset(self):
		return PartyList.objects.filter(owner=self.request.user)

class PartyListCreateView(LoginRequiredMixin, CreateView):
	form_class = PartyListCreateForm
	template_name = 'form.html'

	def form_valid(self, form):
		instance = form.save(commit=False)
		instance.owner = self.request.user
		return super(PartyListCreateView, self).form_valid(form)

	# context for html title
	def get_context_data(self, *args, **kwargs):
		context = super(PartyListCreateView, self).get_context_data(*args, **kwargs)
		context['title'] = 'Add Party List'
		return context

class PartyListUpdateView(LoginRequiredMixin, UpdateView):
	form_class = PartyListCreateForm
	template_name = 'partylists/detail-update.html'

	# context for html title
	def get_context_data(self, *args, **kwargs):
		context = super(PartyListUpdateView, self).get_context_data(*args, **kwargs)
		name = self.get_object().partylist_name
		context['title'] = 'Update Party List:%s'% name
		return context

	def get_queryset(self):
		return PartyList.objects.filter(owner=self.request.user)