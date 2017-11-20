from django.core.urlresolvers import reverse_lazy
from django.views.generic import (TemplateView,
                                ListView,DetailView,
                                CreateView,DeleteView,
                                UpdateView)
from . import models


class IndexView(TemplateView):
    template_name = 'index.html'


class AnimalListView(ListView):
    model = models.Animal


class AnimalDetailView(DetailView):
    context_object_name = 'animal_details'
    model = models.Animal
    template_name = 'basic_app/animal_detail.html'


class AnimalCreateView(CreateView):
    fields = ("name","age","owner")
    model = models.Animal


class AnimalUpdateView(UpdateView):
    fields = ("name", "age")
    model = models.Animal


class AnimalDeleteView(DeleteView):
    model = models.Animal
    success_url = reverse_lazy("basic_app:list")

