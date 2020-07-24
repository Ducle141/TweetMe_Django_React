# from __future__ import unicode_literals
import random
from django.shortcuts import render, redirect

from django.shortcuts import render
from .forms import TweetForm
from .forms import Tweet


def index(request):
    form = TweetForm()
    context = {'form': form}
    return render(request, 'index.html')