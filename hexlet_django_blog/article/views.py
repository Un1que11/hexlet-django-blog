from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView

from hexlet_django_blog.article.models import Article
from hexlet_django_blog.article.forms import ArticleForm


class IndexView(ListView):
    model = Article
    template_name = 'article/index.html'


class ArticleCreate(CreateView):

    def get(self, request, *args, **kwargs):
        form = ArticleForm()
        return render(request, 'article/create.html', context={
            'form': form
        })

    def post(self, request, *args, **kwargs):
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')

        return render(request, 'article/create.html', context={
            'form': form,
        })


class ArticleUpdate(UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = 'article/update.html'


class ArticleDelete(DeleteView):
    model = Article
    success_url = reverse_lazy('articles:index')
    template_name = 'article/delete.html'


class ArticleDetail(DetailView):
    model = Article
    template_name = 'article/show.html'
