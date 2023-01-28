from django import forms

from hexlet_django_blog.article.models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['name', 'body']
