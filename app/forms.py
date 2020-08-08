from django import forms
from django.forms import ModelForm
from .models import Tweet

MAX_TWEET_LENGTH = 2400

class TweetForm(ModelForm):
    class Meta:
        model = Tweet
        fields = ['content']
    def clean_content(self):
        content = self.cleaned_data_content().get("content")
        if len(content) > MAX_TWEET_LENGTH:
            raise forms.ValidationError("This tweet is too long")
        return content
