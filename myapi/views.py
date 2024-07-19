from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
import posixpath
from pathlib import Path

from django.utils._os import safe_join
from django.views.static import serve as static_serve

from .models import MealPost
from .serializers import MealSerializer

class meals_list(viewsets.ModelViewSet):
    serializer_class = MealSerializer
    queryset = MealPost.objects.all()

def serve_webpage(request, path, document_root=None):
    path = posixpath.normpath(path).lstrip("/")
    fullpath = Path(safe_join(document_root, path))
    if fullpath.is_file():
        return static_serve(request, path, document_root)
    else: 
        return static_serve(request, "index.html", document_root)
