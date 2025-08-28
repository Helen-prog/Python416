from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Profile, Skill, Message


class MessageForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for fields in self.fields.values():
            fields.widget.attrs.update({'class': 'input'})

    class Meta:
        model = Message
        fields = ['name', 'email', 'subject', 'body']


class SkillForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for fields in self.fields.values():
            fields.widget.attrs.update({'class': 'input'})

    class Meta:
        model = Skill
        fields = '__all__'
        exclude = ['owner']


class ProfileForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for fields in self.fields.values():
            fields.widget.attrs.update({'class': 'input'})

    class Meta:
        model = Profile
        fields = ['name', 'email', 'username', 'bio', 'short_intro', 'profile_image', 'social_github', 'social_youtube', 'social_website']


class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for fields in self.fields.values():
            fields.widget.attrs.update({'class': 'input'})

    class Meta:
        model = User
        fields = ['first_name', 'email', 'username', 'password1', 'password2']
        labels = {'first_name': 'Name'}

