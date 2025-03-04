import subprocess

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from django.core.paginator import Paginator
from .models import ReviewModel


# Create your views here.
def hello_world(request) :
    return HttpResponse('<h2>hello world from Review_app!!!</h2>')

def test_login_view(request):
    return render(request, 'test_login.html')

def input_scraping_view(request):
    return render(request, 'input_scraping.html')

# LoginRequiredMixin:要認証
class ListReView(LoginRequiredMixin, ListView) :
    template_name = 'review_list.html'
    model = ReviewModel
    # 1ページあたりの表示件数
    # paginate_by = 20

    def get_queryset(self):
        queryset = super().get_queryset()
        # ここでデータを編集します
        for obj in queryset:
            # 商品名は27文字以降カット（長いので）
            obj.item_nm = obj.item_nm[:27] + "…"
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # デフォルトの表示件数を25に設定
        page_size = self.request.GET.get('page_size', 25)

        paginator = Paginator(self.get_queryset(), page_size)
        page = self.request.GET.get('page')

        context['page_obj'] = paginator.get_page(page)
        context['page_size'] = page_size

        return context


class DashBoardView(LoginRequiredMixin, ListView) :
    template_name = 'dashboard.html'
    model = ReviewModel

def run_scraping(request):
    """
    楽天レビューのスクレイピングプログラムをキックする
    :param request:
    :return: なし
    """
    if request.method == 'POST':

        arg1 = str(request.POST.get('name-rak-url'))
        arg2 = request.POST.get('name-rak-page')
        arg3 = str(request.user.id) #

        # サブプロセスを使ってスクリプトを実行する
        result = subprocess.run(['python', 'scraping/review.py', arg1, arg2, arg3]
                                , stdout=subprocess.PIPE
                                , shell=True
                                , text=True
                                )

        # スクリプトの出力とリターンコードを取得
        # output = result.stdout
        # return_code = result.returncode

        return HttpResponse("Script executed successfully. : "
                            "ReturnCode : " + str(result.returncode) + "\n"
                             + "Outmsg : " + str(result.stdout) + "\n"
                             + "Errmsg : " + str(result.stderr)
                            )

    #Get時は何もせず、返して終了
    return render(request, 'dashboard.html')



