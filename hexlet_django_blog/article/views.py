from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse


class Index(View):

    def get(self, request, tags, article_id):
        # return redirect('article', tags='python', article_id=42)
        return render(
            request,
            'article/index.html',
            context={
                'name': 'hexlet django blog',
                'tags': tags,
                'article_id': article_id
            })
