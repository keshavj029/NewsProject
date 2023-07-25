from django.shortcuts import render
from django.views import generic
from .models import Post








# def home(request):
#     return render(request, 'newsapp/home.html')

# def summary(request):
#     return render(request, 'newsapp/postpage.html')

def sentiment(request):
    return render(request, 'newsapp/sentiment.html')
def keyword(request):
    return render(request, 'newsapp/keyword.html')

def classification(request):
    return render(request, 'newsapp/classification.html')




class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

# Create your views here.
