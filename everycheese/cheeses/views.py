from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin


from .models import Cheese

class CheeseListView(ListView):
    model = Cheese

class CheeseDetailView(DetailView):
    model = Cheese
    context_object_name = 'cheese'
class CheeseCreateView(LoginRequiredMixin, CreateView):    
    model = Cheese
    fields = [ 'name','description','firmness','country_of_origin',]
    