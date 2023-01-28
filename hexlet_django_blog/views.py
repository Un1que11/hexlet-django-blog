from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView


class Index(TemplateView):

    template_name = 'index.html'


def about(request):
    return render(request, 'about.html')
