from django.shortcuts import render

# Create your views here.

def searchLecture(request):
    return render(request, 'search.html')