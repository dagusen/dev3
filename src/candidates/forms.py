from django import forms

from .models import Candidate

class CandidateCreateForm(forms.ModelForm):
	class Meta:
			model = Candidate
			fields = [
				'user',
				'positionNpartylist'
			]