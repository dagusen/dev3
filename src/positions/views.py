# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import (
	ListView, 
	DetailView, 
	CreateView, 
	UpdateView,
	View
	)

from .forms import PositionCreateForm

from .models import Position

# Create your views here.

class PositionListView(LoginRequiredMixin, ListView):
	def get_queryset(self):
		return Position.objects.filter(user=self.request.user)

class PositionDetailView(LoginRequiredMixin, DetailView):
	def get_queryset(self):
		return Position.objects.filter(user=self.request.user)

class PositionCreateView(LoginRequiredMixin, CreateView):
	form_class = PositionCreateForm
	template_name = 'form.html'

	#validating user
	def form_valid(self, form):
		obj = form.save(commit=False)
		obj.user = self.request.user
		return super(PositionCreateView, self).form_valid(form)

	def get_queryset(self):
		return Position.objects.filter(user=self.request.user)

	def get_context_data(self, *args, **kwargs):
		context = super(PositionCreateView, self).get_context_data(*args, **kwargs)
		context['title'] = 'Add Position'
		return context

	#for user checking if login of not
	#giving data
	# def get_form_kwargs(self):
	#  	kwargs = super(PositionCreateView, self).get_form_kwargs()
	#  	kwargs['user'] = self.request.user
	#  	return kwargs

class PositionUpdateView(LoginRequiredMixin, UpdateView):
	form_class = PositionCreateForm
	template_name = 'positions/detail-update.html'
	def get_queryset(self):
		return Position.objects.filter(user=self.request.user)

	# context for html title
	def get_context_data(self, *args, **kwargs):
		context = super(PositionUpdateView, self).get_context_data(*args, **kwargs)
		context['title'] = 'Update Position'
		return context

	#for user checking if login of not
	#giving data
	# def get_form_kwargs(self):
	# 	kwargs = super(PositionUpdateView, self).get_form_kwargs()
	# 	kwargs['user'] = self.request.user
	# 	return kwargs