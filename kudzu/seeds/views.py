from django.shortcuts import render
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
