from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView


class Index(TemplateView):

    template_name = 'index.html'

    def render_to_response(self, context, **response_kwargs):
        # return redirect('article', tags='python', article_id=42)
        return redirect(reverse_lazy('article', kwargs={'tags': 'python', 'article_id': 42}))
        # context = super().get_context_data()
        # context['who'] = 'World'
        # return context


def about(request):
    return render(request, 'about.html')
