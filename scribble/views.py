from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm, CommentForm

# Create your views here.
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'scribble/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = Post.objects.get(id=pk)
    return render(request, 'scribble/post_detail.html', {'post': post})

def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'scribble/post_form.html', {'form': form}) 

def comment_create(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save()
            return redirect('post_detail', pk=comment.post.pk)
    else:
        form = CommentForm()
    return render(request, 'scribble/comment_create.html', {'form': form})

        
