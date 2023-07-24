from django.shortcuts import render

def home(request):
    return render(request, 'newsapp/home.html')

def summary(request):
    return render(request, 'newsapp/summary.html')

def sentiment(request):
    return render(request, 'newsapp/sentiment.html')
def keyword(request):
    return render(request, 'newsapp/keyword.html')

def classification(request):
    return render(request, 'newsapp/classification.html')


# Create your views here.
