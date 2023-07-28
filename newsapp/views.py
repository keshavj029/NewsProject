from django.shortcuts import render, redirect,HttpResponse
from django.views import generic
from .models import Post
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required









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
    post_list = Post.objects.all() 
    template_name = 'newsapp/index.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'newsapp/post_detail.html'

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
        



    return render (request,'signup.html')
        



    

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'login.html')

# Create your views here.
