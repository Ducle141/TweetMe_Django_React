from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create_tweet', views.create_tweet, name='create_tweet'),
    path("tweets", views.tweet_list_view, name="tweet_list_view"),
    path('api/delete/<int:tweet_id>', views.tweet_delete, name='delete_tweet'),
    path('api/action', views.action, name='action'),
]