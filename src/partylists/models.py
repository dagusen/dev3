# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.conf import settings

from django.db.models.signals import pre_save

from django.db.models import Q

from django.core.urlresolvers import reverse

from .utils import unique_slug_generator

User = settings.AUTH_USER_MODEL

# Create your models here.

class CandidateQuerySet(models.query.QuerySet):
	def search(self, query): #RestaurantLocation.objects.all().search(query)
		if query:
			query = query.strip()
			return self.filter(
				Q(partylist_name__icontains=query)|
				Q(partylist_name__iexact=query)|
				Q(position__position_name__icontains=query)|
				Q(position__position_name__iexact=query)
				).distinct()
		return self
#search
class CandidateManager(models.Manager):
	def get_queryset(self): #RestaurantLocation.objects.search()
		return CandidateQuerySet(self.model, using=self._db)

	def search(self, query):
		return self.get_queryset().search(query)

class PartyList(models.Model):
	owner 				= models.ForeignKey(User)
	partylist_name 		= models.CharField(max_length=120)
	timestamp			= models.DateTimeField(auto_now_add=True)
	updated				= models.DateTimeField(auto_now=True)
	slug				= models.SlugField(null=True, blank=True)

	objects 			= CandidateManager()

	def __str__(self):
		return self.partylist_name

	class Meta:
		ordering = ['-updated', '-timestamp']

	def get_absolute_url(self):
		return reverse('party-list:edit', kwargs={'slug': self.slug})

	@property
	def title(self):
		return self.partylist_name

def rl_pre_save_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = unique_slug_generator(instance)

pre_save.connect(rl_pre_save_receiver, sender=PartyList)