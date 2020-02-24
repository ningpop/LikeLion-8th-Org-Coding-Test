from django.shortcuts import render, get_object_or_404, redirect
from .models import Lecture, LectureRequest
from django.utils import timezone
from django.core.paginator import Paginator

# Create your views here.

# 지정된 page
# 강의 추가 요청 목록 page
def addLecture(request):
    request_list = LectureRequest.objects.all()
    paginator = Paginator(request_list, 10)
    page = request.GET.get('page')
    requests = paginator.get_page(page)
    return render(request, 'add.html', {'requests': requests})

# 강의 추가 요청 글 Create page
def lectureRequest(request):
    return render(request, 'request.html')

# 강의 추가 요청 글 Read page
def requestDetail(request, request_id):
    request_detail = get_object_or_404(LectureRequest, pk=request_id)
    return render(request, 'request_detail.html', {'request_detail': request_detail})

# page에서 기능 수행
# 강의 추가 요청 글 Create
def lecture_request(request):
    if request.method == 'POST':
        lecture_request = LectureRequest()
        lecture_request.title = request.POST['lecture_name']
        lecture_request.professor = request.POST['professor_name']
        lecture_request.user = request.user
        lecture_request.created_at = timezone.datetime.now()
        lecture_request.save()
        return redirect('/add/request/detail/' + str(lecture_request.id))
    else:
        return redirect('/add/')


# 신규 강의 create
def lecture_submit(request):
    if request.method == 'POST':
        lecture = Lecture()
        lecture.title = request.POST['lecture_name']
        lecture.professor = request.POST['professor_name']
        lecture.save()
        return redirect('/search/detail/' + str(lecture.id))
    else:
        return redirect('home')