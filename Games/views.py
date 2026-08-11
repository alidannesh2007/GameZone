from django.shortcuts import render,get_object_or_404, redirect
from django.http import HttpResponse
from .models import *
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin


class game_List_View(ListView):
    model = game
    template_name = 'home.html'
    context_object_name = 'games'
    def get_queryset(self):
        return game.objects.all()[0:3]


class games_List_View(ListView):
    model = game
    template_name = 'games.html'
    context_object_name = 'games'
    paginate_by = 8


class game_Detail_View(DetailView):
    model = game
    template_name = 'game_info.html'
    context_object_name = 'game'
    
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['comments'] = comment.objects.filter(game_name = self.object)
        return context



class commentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = comment
    template_name = 'comment.html'
    fields = ['comment']
    
    
    def form_valid(self, form):
        
        form.instance.user = self.request.user
        form.instance.game_name = get_object_or_404(game, pk =self.kwargs['pk'])
    
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('Game information', kwargs={'pk': self.object.game_name.pk})
    
    def test_func(self):
        comment = self.get_object()
        
        return self.request.user == comment.user
        

class commentCreateView(LoginRequiredMixin, CreateView):
    model = comment
    template_name = 'comment.html'
    fields = ['comment']
    
    
    def form_valid(self, form):
        
        form.instance.user = self.request.user
        form.instance.game_name = get_object_or_404(game, pk =self.kwargs['pk'])
    
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('Game information', kwargs={'pk': self.object.game_name.pk})
    
    # def test_func(self):
    #     comment = self.get_object()
        
    #     return self.request.user == comment.user



class commentDeleteClass(DeleteView):
    model = comment
    template_name = 'delete_comment.html'
    context_object_name = 'comment'
    # success_url = 'Game/<int:pk>'
    
    def get_success_url(self):
        return reverse_lazy(
            'Game information',
            kwargs={'pk': self.object.game_name.pk}
        )