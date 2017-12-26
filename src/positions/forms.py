from django import forms

from .models import Position

class PositionCreateForm(forms.ModelForm):
	class Meta:
		model = Position
		fields = [
			'partylist',
			'position_name'
		]