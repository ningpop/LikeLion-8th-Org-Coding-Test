from django.shortcuts import render, get_object_or_404
from .models import Lecture

# Create your views here.

def searchLecture(request):
    lecture_list = Lecture.objects.all().order_by('-id')
    return render(request, 'search.html', {'lecture_list': lecture_list})

def detailLecture(request, lecture_id):
    lecture_detail = get_object_or_404(Lecture, pk=lecture_id)
    return render(request, 'detail.html', {'lecture': lecture_detail})