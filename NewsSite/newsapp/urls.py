
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name = 'home'),
    path("summary", views.summary, name = 'News Summary'),
    path("sentiment", views.sentiment, name = 'SentimentAnalysis'),
    path("keyword", views.keyword, name = "Keyword Extraction"),
    path("classification", views.classification, name = "Text classification")
]