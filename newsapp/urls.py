
from django.urls import path
from . import views



urlpatterns = [
    path('', views.PostList.as_view(), name = 'home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name = 'post_detail'),


    



    path("sentiment", views.sentiment, name = 'SentimentAnalysis'),
    path("keyword", views.keyword, name = "Keyword Extraction"),
    path("classification", views.classification, name = "Text classification"),
]