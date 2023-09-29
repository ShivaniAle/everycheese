from django.shortcuts import render
from django.urls import reverse
from django.views.generic import (ListView, DetailView, CreateView, UpdateView)
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from everycheese.cheeses.models import Cheese

from .models import Cheese

class CheeseListView(ListView):
    model = Cheese

class CheeseDetailView(DetailView):
    model = Cheese
    context_object_name = 'cheese'

class CheeseDeleteView(LoginRequiredMixin, DeleteView):
    model = Cheese
    success_url = reverse_lazy('cheeses:list')


class CheeseCreateView(LoginRequiredMixin, CreateView):    
    model = Cheese
    fields = [ 'name','description','firmness','country_of_origin',]
    
    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)

class CheeseUpdateView(LoginRequiredMixin, UpdateView):
    model = Cheese
    fields = [
        'name',
        'description',
        'firmness',
        'country_of_origin'
    ]
    action = "Update"
