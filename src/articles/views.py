"""imports"""
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.http import Http404
from django.contrib import messages

from . import forms
from .models import Article


def article_list(request):
    articles = Article.objects.filter(draft=False).filter(publish__lte=timezone.now()).order_by('publish')
    
    if request.user.is_authenticated:
        
        user_articles = Article.objects.filter(author=request.user).order_by('publish')
        context = {
            "title": "Article List",
            "articles": articles,
            "user_articles": user_articles
        }
    else:
        context = {
            "title": "Article List",
            "articles": articles,
        }
    
    return render(request, "articles/article_list.html", context)


def article_details(request, slug):
    instance = get_object_or_404(Article, slug=slug)      
    context = {
        "article": instance,
        "title": instance.title
    }
    return render(request, "articles/article_details.html", context)


@login_required(login_url="/accounts/login/")
def article_create(request):
    form = forms.ArticleForm()
    if request.method == 'POST':
        form = forms.ArticleForm(request.POST, request.FILES)
        if form.is_valid():

            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            messages.success(request, "Successfully created")
            return redirect('articles:list')
    else:
        form = forms.ArticleForm()

    return render(request, 'articles/article_create.html', {'form': form})


def article_edit(request, slug):
    instance = get_object_or_404(Article, slug=slug)
    if not (instance.author == request.user or request.user.is_superuser or request.user.is_staff):
        raise Http404
        
    form = forms.ArticleForm(instance=instance)

    context = {
        "title": instance.title,
        "article": instance,
        "form": form
    }

    if request.method == 'POST':
        form = forms.ArticleForm(
            request.POST, request.FILES, instance=instance)
        if form.is_valid():
            instance = form.save(commit=True)
            #success
            messages.success(request, "<a href='#'>Item</a> Saved", extra_tags='html_safe')
            return redirect('articles:list')
    else:
        form = forms.ArticleForm()

    return render(request, 'articles/article_edit.html', context)


def article_delete(request, slug):
    instance = get_object_or_404(Article, slug=slug)
    if not (instance.author == request.user.username or request.user.is_superuser or request.user.is_staff):
        raise Http404
    instance.delete()
    messages.success(request, "Successfully deleted")
    return redirect("articles:list")
