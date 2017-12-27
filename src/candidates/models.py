# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.db.models.signals import post_save

from django.conf import settings

User = settings.AUTH_USER_MODEL

# Create your models here.

class CandidateManager(models.Manager):
	def toggle_vote(self, request_user, username_to_toggle):
		candidate_ = Candidate.objects.get(user__username__iexact=username_to_toggle)
		user = request_user
		is_voted = False
		if user in candidate_.voters.all():
			candidate_.voters.remove(user)
		else:
			candidate_.voters.add(user)
			is_voted = True
		return candidate_, is_voted

class Candidate(models.Model):
	user 				= models.OneToOneField(User)
	voters				= models.ManyToManyField(User, related_name='is_voted', blank=True)
	activation_key 		= models.CharField(max_length=120, blank=True, null=True)
	activated			= models.BooleanField(default=False)
	timestamp			= models.DateTimeField(auto_now_add=True)
	updated				= models.DateTimeField(auto_now=True)

	objects 			= CandidateManager()

	def __str__(self):
		return self.user.username

def post_save_user_receiver(sender, instance, created, *args, **kwargs):
	if created:
		candidate, is_created = Candidate.objects.get_or_create(user=instance)

post_save.connect(post_save_user_receiver, sender=User)