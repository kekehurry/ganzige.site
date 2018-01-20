from django.shortcuts import render

# Create your views here.
def aria2(request):
    return render(request,'aria2/index.html')
