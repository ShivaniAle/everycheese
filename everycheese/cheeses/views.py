from django.shortcuts import render
from django.urls import reverse

from django.views.generic import (ListView, DetailView, CreateView, UpdateView)
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect, render
from everycheese.cheeses.models import Cheese, Rating
from .forms import RatingForm

from django.views import View

from django.db.models import Avg  # Add this import


from .models import Cheese
import logging  # Import the logging module


#Create a logger object
log = logging.getLogger("root")

class CheeseListView(ListView):
    model = Cheese

class CheeseDetailView(DetailView):
    model = Cheese

class CheeseDeleteView(LoginRequiredMixin, DeleteView):
    model = Cheese
    success_url = reverse_lazy('cheeses:list')
    template_name = 'cheeses/cheese_confirm_delete.html'


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

    def get_context_data(self, **kwargs):
        log.info("FOUND RATING")
        ctx = super(CheeseUpdateView, self).get_context_data(**kwargs)
        _slug = self.kwargs.get("slug")
        ch = Cheese.objects.all().filter(slug = _slug).first()

        if ch == None:
            ctx["rating"] = 0
            return

        r = Rating.objects.all().filter(creator = self.request.user,cheese = ch).first()

        if r != None:
            ctx["rating"] = r.i_rating
        else:
            ctx["rating"] = 0

        return ctx

    def get_success_url(self):
        return reverse('cheeses:detail', args=[str(self.object.slug)])
