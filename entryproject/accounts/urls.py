from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from .views import SignUpView, SignUpSuccessView

app_name = 'accounts'

# appのURLSルーティング設定
urlpatterns = [
    path('signup/', SignUpView.as_view() , name='signup') ,
    path('signup_success/', SignUpSuccessView.as_view() , name='signup_success') ,
    path('login/', LoginView.as_view(template_name='login.html'), name='login' ) ,
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout' ),
]
