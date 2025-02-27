from django.urls import path
from .views import hello_world, run_scraping, test_login_view, input_scraping_view
from .views import DashBoardView, ListReView

# appのURLSルーティング設定
urlpatterns = [
    path('hello/', hello_world, name='hello_world') ,
    path('dashboard/', DashBoardView.as_view(), name='dashboard') ,
    path('run_script/', run_scraping, name='run_script'),
    path('test_login/', test_login_view, name='test_login'),
    path('input_scraping/', input_scraping_view, name='input_scraping'),
    path('review_list/', ListReView.as_view(), name='review_list'),
]
