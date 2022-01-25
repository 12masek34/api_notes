from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api.views import *

urlpatterns = [
    path('notes/', NoteListView.as_view()),
    path('notes/<int:pk>', NoteDetailView.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)