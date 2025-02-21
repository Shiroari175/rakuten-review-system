import subprocess

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

def run_scraping(request):
    """
    楽天レビューのスクレイピングプログラムをキックする
    :param request:
    :return: なし
    """
    if request.method == 'POST':

        # 引数を指定してスクリプトを実行
        arg1 = 'https://review.rakuten.co.jp/item/1/236315_10011235/1.1/'
        arg2 = '1'
        arg3 = str(request.user.id)

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



