from django.shortcuts import render, get_object_or_404, redirect
from .models import Lecture, Review
from django.utils import timezone
from django.core.paginator import Paginator

# Create your views here.

# 지정된 page
# 강의 목록 page
def boardLecture(request):
    lecture_list = Lecture.objects.all().order_by('-id')
    paginator = Paginator(lecture_list, 6)
    page = request.GET.get('page')
    lectures = paginator.get_page(page)
    return render(request, 'board.html', {'lectures': lectures})

# 강의평 Read page
def detailLecture(request, lecture_id):
    lecture_detail = get_object_or_404(Lecture, pk=lecture_id)
    return render(request, 'detail.html', {'lecture': lecture_detail})

# 강의평 Create page
def evaluateLecture(request, lecture_id):
    lecture_evaluate = get_object_or_404(Lecture, pk=lecture_id)
    return render(request, 'evaluate.html', {'lecture': lecture_evaluate})


# page에서 기능 수행
# 검색결과 찾기
def lecture_search(request):
    lecture_list = Lecture.objects.all()
    keyword = request.GET.get('search', '')
    if keyword:
        lecture_list = lecture_list.filter(title__icontains=keyword)
    return render(request, 'board.html', {'lecture_list': lecture_list})

# 강의 Delete
def lecture_delete(request, lecture_id):
    lecture = get_object_or_404(Lecture, pk=lecture_id)
    lecture.delete()
    return redirect('/search/board/')

# Review 등록
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

# Review 삭제
def review_delete(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    lecture = get_object_or_404(Lecture, pk=review.lecture.id)
    review.delete()
    return redirect('/search/detail/' + str(review.lecture.id))