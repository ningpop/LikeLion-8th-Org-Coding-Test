from django.shortcuts import render

# Create your views here.

def addLecture(request):
    return render(request, 'add.html')