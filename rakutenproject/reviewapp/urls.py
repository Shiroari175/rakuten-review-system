from django.urls import path
from .views import hello_world, run_scraping
# from .views import hello_world, CreateEntryView, UserView, UpdateEntryView, DeleteEntryView
from .views import DashBoardView

# appのURLSルーティング設定
urlpatterns = [
    path('hello/', hello_world, name='hello_world') ,
    path('dashboard/', DashBoardView.as_view(), name='dashboard') ,
    path('run_script/', run_scraping, name='run_script'),
]
