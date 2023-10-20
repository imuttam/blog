from django.shortcuts import render, get_list_or_404

from .models import Post 

def post_list(request):
  posts = Post.objects.all()
  return render(request, 'blog/list.html',{'posts':posts})


def post_detail(request, id):
  post = get_list_or_404(Post, 
                         id=id, status=Post.Status.PUBLISHED)
    
  return render(request, 'blog/detail.html', {'post':post})