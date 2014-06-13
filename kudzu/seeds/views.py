import requests

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Seed, Question, Reply


def home(request):
    return render(request, 'index.html')

def article(request):
    return render(request, 'article.html')

def show_seed(request, seed_id):
    seed = get_object_or_404(Seed, id=int(seed_id))
    return render(request, 'seeds/show.html', {'seed': seed})


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
