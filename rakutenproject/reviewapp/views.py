from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import ReviewModel


# Create your views here.
def hello_world(request) :
    return HttpResponse('<h2>hello world from Review_app!!!</h2>')

# LoginRequiredMixin:要認証
class DashBoardView(LoginRequiredMixin, ListView) :
    template_name = 'dashboard.html'
    model = ReviewModel

