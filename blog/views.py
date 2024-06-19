from django.shortcuts import render
from django.template.defaultfilters import slugify
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from blog.models import Blog


class SetSlugMixin:
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.slug = slugify(obj.title)
        obj.save()
        return super().form_valid(form)

class BlogCreateView(SetSlugMixin, CreateView):
    model = Blog
    fields = ('title', 'content', 'is_published',)
    success_url = reverse_lazy('blog:blog_list')


class BlogListView(ListView):
    model = Blog

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset()
        queryset = queryset.filter(is_published=True)
        return queryset


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class BlogUpdateView(SetSlugMixin, UpdateView):
    model = Blog
    fields = ('title', 'content', 'is_published',)
    success_url = reverse_lazy('blog:blog_list')

    def get_success_url(self):
        return reverse('blog:blog_detail', args=(self.kwargs['pk'],))


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:blog_list')

