# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from .forms import PostForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

def public_list(request):
    posts = Post.objects.filter(is_public=True).order_by('created_date')
    #TODO: 特定推送功能
    return render(request, 'diary/public_list.html', {'posts': posts})

@login_required
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    # TODO: 特定推送功能
    return render(request, 'diary/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'diary/post_detail.html', {'post': post})

@login_required
def post_new(request):
    if request.method == "POST":
        post = PostForm(request.POST)
        if post.is_valid():
            post = post.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)

    else:
        post = PostForm()

    return render(request, 'diary/post_edit.html', {'post': post})

@login_required
def post_edit(request, pk):

    post = get_object_or_404(Post, pk=pk)

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)

    return render(request, 'diary/post_edit.html', {'form': form})

@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')

