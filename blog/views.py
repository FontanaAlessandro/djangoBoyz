from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):
    posts = Post.objects.filter(data_pubblicazione__lte=timezone.now()).order_by('data_pubblicazione')
    return render(request, 'blog/post_list.html', {'posts': posts})
