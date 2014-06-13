import requests

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Seed, Question, Reply


def home(request):
    return render(request, 'index.html')


@csrf_exempt
def create(request):
    seed = Seed.objects.create(
        url=request.POST.get('url', 'http://'),
        user=request.user
    )
    question = Question(seed=seed)
    question.save()
    question.video.save('video.webm', request.FILES['file'])
    return render(request, 'seeds/upload.html')


def user_latest(request, user_id):
    response = requests.get('https://api.vineapp.com/timelines/users/' + user_id)
    return HttpResponse(response.text)


def vine_video(request, video_id):
    response = requests.get('https://api.vineapp.com/timelines/posts/' + video_id)
    return HttpResponse(response.text)
