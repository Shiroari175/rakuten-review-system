from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import EntryModel

# Create your views here.

def hello_world(request) :
    return HttpResponse('<h2>hello world from entryapp!!!</h2>')

# LoginRequiredMixin:要認証
class ListEntryView(LoginRequiredMixin, ListView) :
    template_name = 'entry/entry_model_list.html'
    model = EntryModel

class DetailEntryView(LoginRequiredMixin, DetailView) :
    template_name = 'entry/entry_detail.html'
    model = EntryModel

class CreateEntryView(LoginRequiredMixin, CreateView) :
    template_name = 'entry/entry_create.html'
    model = EntryModel
    fields = ['title', 'entry_text']
    success_url = reverse_lazy('list_entry')

    def form_valid(self, form):
        entry = form.save(commit=False)
        entry.user = self.request.user
        entry.save() # ここでデータをセーブ
        return super().form_valid(form)


class UserView(LoginRequiredMixin, ListView) :
    template_name = 'entry/entry_model_list.html'
    paginate_by = 9
    # model = EntryModel

    def get_queryset(self):
        user_id = self.kwargs['user']
        user_list = EntryModel.objects.filter(user = user_id)
        return user_list


class UpdateEntryView(LoginRequiredMixin, UpdateView) :
    """
     投稿記事の更新処理
     要認証
    """
    template_name = 'entry/entry_update.html'
    model = EntryModel
    fields = ['title', 'entry_text']
    success_url = reverse_lazy('list_entry')

    # 自分の記事以外は編集できないようにする
    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.user != self.request.user :
            raise PermissionDenied
        return obj


class DeleteEntryView(LoginRequiredMixin, DeleteView) :
    """
     投稿記事の削除処理
     要認証
    """
    template_name = 'entry/entry_delete.html'
    model = EntryModel
    success_url = reverse_lazy('list_entry')

    # 自分の記事以外は編集できないようにする
    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.user != self.request.user :
            raise PermissionDenied
        return obj

