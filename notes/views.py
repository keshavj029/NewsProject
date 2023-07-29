from django.shortcuts import render
from .models import Notes
from django.http import Http404


from django.views.generic import ListView, DetailView, CreateView,UpdateView
from .forms import NotesForm



from django.views.generic.edit import DeleteView



class NotesDeleteView(DeleteView):
    model = Notes
    context_object_name = "/smart/notes"
    template_name= 'notes_delete.html'
    success_url = '/smart/notes'



class NotesListView(ListView):
    model = Notes
    context_object_name = "notes"
    template_name= 'notes_list.html'

    
class NotesDetailView(DetailView):
    model = Notes
    context_object_name = "note"
    template_name= 'notes_details.html'


class NotesCreateView(CreateView):
    model = Notes
    form_class = NotesForm
    success_url = '/smart/notes'
    template_name= 'notes_form.html'



class NotesUpdateView(UpdateView):
    model = Notes
    
    success_url ='/smart/notes'
    form_class = NotesForm
    template_name= 'notes_form.html'
