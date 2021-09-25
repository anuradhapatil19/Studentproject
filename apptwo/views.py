from django.shortcuts import render
from django.urls import reverse_lazy

from .models import Product
# Create your views here.
from django.views.generic import CreateView,ListView,DetailView

class create_product(CreateView):
    model = Product
    fields = '__all__'
    success_url = reverse_lazy('pd')

class list_product(ListView):
    model = Product
    fields='__all__'

class detail_product(DetailView):
    model = Product
