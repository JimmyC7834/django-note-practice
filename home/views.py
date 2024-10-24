from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Note
from .forms import NoteForm

class HomeView(TemplateView):
  template_name = "home/welcome.html"

class PrivateView(LoginRequiredMixin, TemplateView):
  template_name = "home/authorized.html"
  login_url = "/admin"

class NotesListView(ListView):
  model = Note
  context_object_name = "notes"

class NoteView(DetailView):
  model = Note
  context_object_name = "note"


class CreateNoteView(CreateView):
  model = Note
  success_url = '/notes/'
  form_class = NoteForm

class UpdateNoteView(UpdateView):
  model = Note
  success_url = '/notes/'
  form_class = NoteForm

class DeleteNoteView(DeleteView):
  model = Note
  success_url = '/notes/'