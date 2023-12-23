from typing import Any
from django.shortcuts import render, redirect
from .models import Snack, Comment, Taste
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


# Create your views here.

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

class SnackList(ListView):
  model = Snack

def snack_detail(request, snack_id):
  snack = Snack.objects.get(id=snack_id)
  id_list = snack.tastes.all().values_list('id')
  taste_not_there = Taste.objects.exclude(id__in=id_list)
  return render(request, 'main_app/snack_detail.html', {
    'snack': snack,
    'tastes': taste_not_there
  })


class SnackCreate(CreateView):
  model = Snack
  fields = '__all__'
  success_url = '/snacks'

class SnackUpdate(UpdateView):
  model = Snack
  fields = ['description', 'prep_time']

class SnackDelete(DeleteView):
  model = Snack
  success_url = '/snacks'


def add_comment(request, object_id):
  snack = Snack.objects.get(id=object_id)
  new_comment = Comment.objects.create(title=request.POST['id_title'], comment=request.POST['id_comment'], snack_id=snack.id)
  new_comment.save()
  return redirect ('snack_detail', snack_id=object_id)

class TasteList(ListView):
  model = Taste

class TasteCreate(CreateView):
  model = Taste
  fields = '__all__'
  success_url = '/tastes'

def assoc_taste (request, snack_id, taste_id):
  Snack.objects.get(id=snack_id).tastes.add(taste_id)
  return redirect('snack_detail', snack_id=snack_id)

def unassoc_taste (request, snack_id, taste_id):
  Snack.objects.get(id=snack_id).tastes.remove(taste_id)
  return redirect('snack_detail', snack_id=snack_id)