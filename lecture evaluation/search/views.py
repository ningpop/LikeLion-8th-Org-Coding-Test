from django.shortcuts import render, get_object_or_404, redirect
from .models import Lecture, Review
from django.utils import timezone

# Create your views here.

def boardLecture(request):
    lecture_list = Lecture.objects.all().order_by('-id')
    return render(request, 'board.html', {'lecture_list': lecture_list})

def detailLecture(request, lecture_id):
    lecture_detail = get_object_or_404(Lecture, pk=lecture_id)
    return render(request, 'detail.html', {'lecture': lecture_detail})

def evaluateLecture(request, lecture_id):
    lecture_evaluate = get_object_or_404(Lecture, pk=lecture_id)
    return render(request, 'evaluate.html', {'lecture': lecture_evaluate})

def lecture_delete(request, lecture_id):
    lecture = get_object_or_404(Lecture, pk=lecture_id)
    lecture.delete()
    return redirect('/search/board/')

# Review

def review(request):
    if request.method == 'POST':
        review = Review()
        review.lecture = Lecture.objects.get(pk=request.POST['lecture'])
        review.user = request.user
        review.created_at = timezone.datetime.now()
        review.personal_score = request.POST['personal_score']
        review.body = request.POST['body']
        review.save()
        return redirect('/search/detail/'+ str(review.lecture.id))
    else:
        return redirect('/search/detail/' + str(review.lecture.id))

def review_delete(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    lecture = get_object_or_404(Lecture, pk=review.lecture.id)
    review.delete()
    return redirect('/search/detail/' + str(review.lecture.id))