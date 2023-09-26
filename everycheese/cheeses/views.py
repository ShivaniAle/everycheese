from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView

from .models import Cheese

class CheeseListView(ListView):
    model = Cheese

class CheeseDetailView(DetailView):
    model = Cheese
    template_name = 'cheeses/cheese_detail.html'
    context_object_name = 'cheese'
class CheeseCreateView(CreateView):
    model = Cheese
    template_name = 'cheeses/cheese_form.html'
    fields = [
            'name',
            'description',
            'firmness',
            'country_of_origin',
    ]
    