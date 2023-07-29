from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView




class HomeView(TemplateView):
    template_name = 'home.html'
    extra_content = {'today':datetime.today()}


class AuthorizedView(LoginRequiredMixin, TemplateView):
    template_name = 'authorised.html'
    login_url = '/admin'

