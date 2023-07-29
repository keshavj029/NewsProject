from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from .models import Notes
from django.http.response import HttpResponseRedirect

from django.views.generic import ListView, DetailView, CreateView,UpdateView
from .forms import NotesForm

from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic.edit import DeleteView




class NotesDeleteView(DeleteView):
    model = Notes
    context_object_name = "/smart/notes"
    template_name= 'notes_delete.html'
    success_url = '/smart/notes'



class NotesListView(LoginRequiredMixin,ListView):
    model = Notes
    context_object_name = "notes"
    template_name= 'notes_list.html'
    login_url="/admin"

    def get_queryset(self):
        return self.request.user.notes.all()

    
class NotesDetailView(DetailView):
    model = Notes
    context_object_name = "note"
    template_name= 'notes_details.html'


class NotesCreateView(LoginRequiredMixin,CreateView):
    model = Notes
    form_class = NotesForm
    success_url = '/smart/notes'
    template_name= 'notes_form.html'
    login_url="/admin"


    def form_valid(self, form):
        
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())



class NotesUpdateView(UpdateView):
    model = Notes
    
    success_url ='/smart/notes'
    form_class = NotesForm
    template_name= 'notes_form.html'
