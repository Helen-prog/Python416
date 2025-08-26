from django.forms import ModelForm
from .models import Project, Review
from django import forms


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['value', 'body']


class ProjectForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for fields in self.fields.values():
            fields.widget.attrs.update({'class': 'input'})

        # self.fields['title'].widget.attrs.update({'class': 'input'})
        # self.fields['description'].widget.attrs.update({'class': 'input'})

    class Meta:
        model = Project
        fields = ['title', 'featured_images', 'description', 'demo_link', 'source_link', 'tags']
        widgets = {'tags': forms.CheckboxSelectMultiple()}


