from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404

def post_list(request):
    posts = Post.objects.filter(data_pubblicazione__lte=timezone.now()).order_by('-data_pubblicazione')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if pk == 1:
        return render(request, 'blog/post_detail.html', {'post': post})
    else:
        return render(request, 'blog/post2_detail.html', {'post': post})
