"""Forms for the Organizer app"""
from django.core.exceptions import ValidationError
from django.forms import ModelForm

from .models import Startup, Tag

class LowercaseNameMixin:
	"""Form cleaner to lower case of name field"""

	def clean_name(self):
		"""Enusre Tag name is always lowercase"""
		return self.cleaned_data["name"].lower()

class SlugCleanMixin:
	"""Mixin class to ensure slug field is not create"""

	def clean_slug(self):
		"""Enusre slug is not 'create'

		This is an oversimplification!!! See the following link for how to raise the error correctly. 

		https://docs.djangoproject.com/en/3.0/ref/forms/validation/#raising-validation-error

		"""
		slug = self.cleaned_data["slug"]
		if slug == "create":
			raise ValidationError(
				"Slug may not be 'create'."
			)
		return slug

class TagForm(LowercaseNameMixin, ModelForm):
	"""HTML form for Tag objects"""

	class Meta:
		model = Tag
		fields = "__all__" # name only, no slug!

class StartupForm(
	LowercaseNameMixin, SlugCleanMixin, ModelForm
):
	"""HTML form for Startup objects"""

	class Meta:
		model = Startup
		fields = "__all__"
