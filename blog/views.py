from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.db.models import F
from django.views import generic
from django.utils import timezone

from .models import Post


# Create your views here.
class LatestIndexView(generic.ListView):
    model = Post
    # By default, the DetailView generic view uses a template called <app name>/<model name>_list.html
    template_name = 'blog/latest.html'
    context_object_name = 'latest_posts_list'

    def get_queryset(self):
        """
        Return the last five published posts (not including those set to be
        published in the future).
        """
        return Post.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]


class IndexView(generic.ListView):
    model = Post
    # By default, the DetailView generic view uses a template called <app name>/<model name>_detail.html
    template_name = 'blog/index.html'
    context_object_name = 'all_posts_list'

    def get_queryset(self):
        """
        Excludes any posts that aren't published yet.
        """
        return Post.objects.filter(pub_date__lte=timezone.now())


class PostView(generic.DetailView):
    model = Post
    # By default, the DetailView generic view uses a template called <app name>/<model name>_detail.html
    template_name = 'blog/post.html'

    def get_queryset(self):
        """
        Excludes any posts that aren't published yet.
        """
        return Post.objects.filter(pub_date__lte=timezone.now())

