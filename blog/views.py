from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from blog.models import Post


# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, "blog/index.html", {"posts": posts})

def post_detail(request, slug_pk):
    post = get_object_or_404(Post, slug=slug_pk)
    return render(request, "blog/post-detail.html", {"post": post})