from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomeView.as_view()),
    path('notes/', views.NotesListView.as_view(), name='note.list'),
    path('notes/new', views.CreateNoteView.as_view(), name='note.new'),
    path('notes/<int:pk>/edit', views.UpdateNoteView.as_view(), name='note.update'),
    path('notes/<int:pk>/delete', views.DeleteNoteView.as_view(), name='note.delete'),
    path('notes/<int:pk>', views.NoteView.as_view(), name="note.details"),
    path('private/', views.PrivateView.as_view()),
]
