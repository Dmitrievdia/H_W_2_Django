from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from blog.models import Article


class ArticleCreateView(CreateView):
    model = Article
    template_name = 'blog/article_form.html'
    fields = ('title', 'content', 'preview', 'published', 'number_views',)
    success_url = reverse_lazy('blog:blog_list')


class ArticleUpdateView(UpdateView):
    model = Article
    fields = ('title', 'content', 'preview', 'published', 'number_views',)
    success_url = reverse_lazy('blog:blog_list')


class ArticleListView(ListView):
    model = Article
    template_name = 'blog/article_list.html'
    context_object_name = 'posts'


class ArticleDetailView(DetailView):
    model = Article
    # template_name = reverse_lazy('blog:article_detail.html')


class ArticleDeleteView(DeleteView):
    model = Article
    success_url = reverse_lazy('blog:blog_list')
