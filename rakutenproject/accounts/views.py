from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from .forms import CustomUserCreationForm


class SignUpView(CreateView) :
    form_class = CustomUserCreationForm
    template_name = "signup.html"
    success_url = reverse_lazy("accounts:signup_success")

    def form_valid(self, form):
        # フォームが正しくバリデーションされた後の処理
        # ここで追加のロジックを実行することもできます
        user = form.save()
        self.object = user
        return super().form_valid(form)


class SignUpSuccessView(TemplateView) :
    template_name = "signup_success.html"

