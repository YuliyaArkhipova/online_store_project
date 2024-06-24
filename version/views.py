from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from version.forms import VersionForm
from version.models import Version


class VersionListView(ListView):
    model = Version
    template_name = 'version/version_list.html'


class VersionDetailView(DetailView):
    model = Version


class VersionCreateView(CreateView):
    model = Version
    form_class = VersionForm
    success_url = reverse_lazy('catalog:product_list')


class VersionUpdateView(UpdateView):
    model = Version
    form_class = VersionForm
    success_url = reverse_lazy('catalog:product_list')