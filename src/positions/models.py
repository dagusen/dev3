# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.db.models.signals import pre_save

from django.conf import settings

from django.core.urlresolvers import reverse

from partylists.models import PartyList

from partylists.utils import unique_slug_generator

User = settings.AUTH_USER_MODEL

# Create your models here.

class Position(models.Model):
	user 				= models.ForeignKey(User)
	partylist			= models.ForeignKey(PartyList)
	position_name 		= models.CharField(max_length=120)
	timestamp			= models.DateTimeField(auto_now_add=True)
	updated				= models.DateTimeField(auto_now=True)
	slug				= models.SlugField(null=True, blank=True)

	def __str__(self):
		return '%s - %s' % (self.position_name, self.partylist )

	def get_absolute_url(self):
		return reverse('position:edit', kwargs={'slug': self.slug})

	@property
	def title(self):
		return self.position_name

	class Meta:
		ordering = ['-updated', '-timestamp']

def rl_pre_save_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = unique_slug_generator(instance)

pre_save.connect(rl_pre_save_receiver, sender=Position)