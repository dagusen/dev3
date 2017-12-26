from django import forms

from .models import PartyList

class PartyListCreateForm(forms.ModelForm):
	class Meta:
			model = PartyList
			fields = [
				'partylist_name'
			]