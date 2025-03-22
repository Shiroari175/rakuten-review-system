from django.urls import path
from .views import hello_world, input_scraping_view, DetailReView
from .views import DashBoardView, ListReView

# appのURLSルーティング設定
urlpatterns = [
    path('hello/', hello_world, name='hello_world') ,
    path('dashboard/', DashBoardView.as_view(), name='dashboard') ,
    path('input_scraping/', input_scraping_view, name='input_scraping'),
    path('review_list/', ListReView.as_view(), name='review_list'),
    path('<int:pk>/review_detail/', DetailReView.as_view(), name='review_detail'),
    # path('modal_data/<int:id>/', ModalDataView.as_view(), name='modal_data'),
    # path('modal_data/', ModalDataView.as_view(), name='modal_data'),
]
