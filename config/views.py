#!/usr/bin/env python3
# Create your views here.
from django.views.generic import ListView

from eijgenraam_nocelery.articles.models import Post


def get_posts():
    return Post.objects.all().order_by("date")


# Create your views here.
class MainPageView(ListView):
    template_name = "pages/home.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "featured_posts"

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(featured=True)
