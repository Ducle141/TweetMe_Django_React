import random

from django.http import JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .forms import TweetForm
from .forms import Tweet
from .serializer import TweetSerializer, TweetActionSerializer

def index(request):
    form = TweetForm()
    context = {'form': form}
    print("Here is my input: " , form)
    return render(request, 'index.html', context)

@api_view(['POST'])
@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
def create_tweet(request):
    '''
    API Endpoint creates new Tweet
    '''
    serializer = TweetSerializer(data=request.POST)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)
        return Response(serializer.data, status=201)
    return Response({}, status=400)

@api_view(['GET'])
def tweet_list_view(request):
    '''
    API endpoint returns all tweets
    '''
    qs = Tweet.objects.all()
    serializer = TweetSerializer(qs, many=True)
    return Response(serializer.data, status=200)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def tweet_delete(request, tweet_id):
    '''
    API Endpoint delete tweets
    '''
    #Check if this tweet_id exists or not
    qs = Tweet.objects.filter(id=tweet_id)
    if not qs.exists():
        return Response({}, status=404)
    #Check if this user are allowed to delete it
    qs = qs.filter(user=request.user)
    if not qs.exists():
        return Response({'You cannot delete this Tweet'})
    obj = qs.first()
    obj.delete()
    return Response ({'message: Tweet removed'}, status=200)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def action(request):
    '''
    Actions are like, unlike, retweet
    '''
    serializer = TweetActionSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):
        print('chao')
        data = serializer.validated_data

        tweet_id = data.get('id')
        action = data.get('action')
        qs = Tweet.objects.filter(id=tweet_id)
        if not qs.exists():
            return Response({}, status=400)
        obj = qs.first()
        if action == 'like':
            obj.likes.add(request.user)
            serializer = TweetSerializer(obj)
            return Response(serializer.data, status=200)
        # elif action == 'unlike':
        #     obj.likes.remove(request.user)
        #     serializer = TweetSerializer(obj)
        #     return Response(serializer.data, status=200)
        elif action == 'retweet':
            new_tweet = Tweet.objects.create(
                user=request.user,
                original=obj,
                content=obj.content
            )
        serializer = TweetSerializer(new_tweet)
        return Response(serializer.data, status=200)


def login (request):
    return render (request, 'login.html')


