from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from .models import Post

# Create your views here.
def index(request):
    all_posts = Post.objects.filter(published=True)
    paginator = Paginator(all_posts, 5)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {
        "latestpost": all_posts.first(),
        "posts": posts,
    }
    return render(request, "updates.html", context)

def post(request, id=None):
    try:
        posts = Post.objects.filter(published=True)[:5]
    except IndexError:
        posts = None
    post = get_object_or_404(Post, ~Q(published=False), id=id)
    context = {
        "latestposts": posts[:5],
        "post": post,
    }
    return render(request, "updatepost.html", context)