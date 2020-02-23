from django.shortcuts import render, get_object_or_404, redirect
from .models import Lecture, Review

# Create your views here.

def searchLecture(request):
    lecture_list = Lecture.objects.all().order_by('-id')
    return render(request, 'search.html', {'lecture_list': lecture_list})

def detailLecture(request, lecture_id):
    lecture_detail = get_object_or_404(Lecture, pk=lecture_id)
    return render(request, 'detail.html', {'lecture': lecture_detail})


# Review

def review(request):
    if request.method == 'POST':
        review = Review()
        review.lecture = Lecture.objects.get(pk=request.POST['lecture'])
        review.personal_score = request.POST['personal_score']
        review.body = request.POST['body']
        revuew.save()
        return redirect('search/detail/'+ str(review.lecture.id))
    else:
        return redirect('home')