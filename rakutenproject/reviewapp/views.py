import subprocess

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator

from .forms import ReviewForm
from .models import ReviewModel
from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
import matplotlib.pyplot as plt
import matplotlib
from io import BytesIO
import base64



# Create your views here.
def hello_world(request) :
    return HttpResponse('<h2>hello world from Review_app!!!</h2>')


def input_scraping_view(request):
    """
    スクレイピング実行
    :param request:
    :return: render:
    """
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            # バリデーション成功
            # フォームのデータを使って何かする
            arg1 = form.cleaned_data['name_rak_url']
            arg2 = form.cleaned_data['name_rak_page']
            arg3 = str(request.user.id)

            # サブプロセスを使ってスクリプトを実行する
            result = subprocess.run(['python','scraping/review.py',
                                        arg1,str(arg2),arg3
                                     ]
                                    , stdout=subprocess.PIPE
                                    , shell=True
                                    , text=True
                                    )
            context = {
                'return_code': str(result.returncode) ,
                'out_msg': result.stdout ,
                'err_msg': result.stderr ,
            }

            return render(request, 'result_scraping.html', context)

        else:
            # バリデーション失敗
            print(form.errors)
    else:
        form = ReviewForm()
        return render(request, 'input_scraping.html', {'form': form})

def output_evaluation_to_star(evaluation):
    """
    評価１～５を☆の数に変換して返す
    :param evaluation:
    :return: star
    """
    e = 0
    star = ""
    while e < 5:
        if e < int(evaluation):
            star += "★"
        else:
            star += "☆"
        e += 1
    return star


# LoginRequiredMixin:要認証
class ListReView(LoginRequiredMixin, ListView) :
    """
    楽天レビュー 一覧表示
    """
    template_name = 'review_list.html'
    model = ReviewModel

    def get_queryset(self):
        queryset = super().get_queryset()

        # 検索ワード取得 部分検索
        query = self.request.GET.get('query', '')
        if query:
            queryset = queryset.filter(item_nm__icontains=query)

        # 評価フィルタ取得
        rating = self.request.GET.get('rating', '')
        if rating:
            queryset = queryset.filter(evaluation=rating)

        # ID sort
        sort_param = self.request.GET.get('sort',None)
        if sort_param in ['id', '-id', 'item_nm', '-item_nm']:
            queryset = queryset.order_by(sort_param)

        # ここでデータを編集
        for obj in queryset:
            # 商品名は27文字以降カット（長いので）
            obj.item_nm = obj.item_nm[:27] + "…"
            # 評価１～５を☆で表現する
            obj.star = output_evaluation_to_star(obj.evaluation)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # デフォルトの表示件数を25に設定
        page_size = self.request.GET.get('page_size', 25)

        # get_queryset()を実行して、ページネーション作成
        paginator = Paginator(self.get_queryset(), page_size)
        page = self.request.GET.get('page')

        context['page_obj'] = paginator.get_page(page)
        context['page_size'] = page_size
        context['query'] = self.request.GET.get('query', '')
        context['rating'] = self.request.GET.get('rating', '')
        # ページ専用のソート情報
        context['page_sort'] = ''

        if self.request.GET.get('sort', None) == 'id':
            context['sort'] = '-id'
            context['page_sort'] = 'id'
        elif self.request.GET.get('sort', None) == '-id':
            context['sort'] = 'id'
            context['page_sort'] = '-id'
        elif self.request.GET.get('sort', None) == 'item_nm':
            context['sort'] = '-item_nm'
            context['page_sort'] = 'item_nm'
        elif self.request.GET.get('sort', None) == '-item_nm':
            context['sort'] = 'item_nm'
            context['page_sort'] = '-item_nm'
        else :
            context['sort'] = ''
            context['page_sort'] = ''

        return context

class DetailReView(LoginRequiredMixin, DetailView) :
    template_name = 'review_detail.html'
    model = ReviewModel

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        # 評価１～５を☆で表現する
        obj.star = output_evaluation_to_star(obj.evaluation)

        return obj

class DashBoardView(LoginRequiredMixin, ListView) :
    """
    ダッシュボード
    """
    model = ReviewModel
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        records = ReviewModel.objects.all()
        unique_records = {record.item_nm: record for record in records}.values()
        context['unique_records'] = unique_records
        return context


@csrf_exempt
def fetch_data(request):
    if request.method == "POST":
        selected_value = request.POST.get("value")

        # 選択された集計グループIDに基づいてクエリを実行
        # result = ReviewModel.objects.filter(group_id=selected_value).first()
        results = ReviewModel.objects.filter(group_id=selected_value)

        # グループ集計用の辞書
        evaluation_groups = {
                    1:{ "star":"★☆☆☆☆", "count":0 } ,
                    2:{ "star":"★★☆☆☆", "count":0 } ,
                    3:{ "star":"★★★☆☆", "count":0 } ,
                    4:{ "star":"★★★★☆", "count":0 } ,
                    5:{ "star":"★★★★★", "count":0 } ,
                }

        # グループ集計を行う
        for obj in results :
            if obj.evaluation in evaluation_groups :
                # print(f"見つかりました！データ: { evaluation_groups[obj.evaluation] }")
                # 見つかったらカウントを＋１する
                evaluation_groups[obj.evaluation]["count"] += 1
            else :
                print("指定したKEYは存在しません。")

        # print(f"結果:{evaluation_groups}")

        # labels = [
        #             "1:★☆☆☆☆",
        #             "2:★★☆☆☆",
        #             "3:★★★☆☆",
        #             "4:★★★★☆",
        #             "5:★★★★★",
        # ]
        # values = [
        #     evaluation_groups[1]["count"] ,
        #     evaluation_groups[2]["count"] ,
        #     evaluation_groups[3]["count"] ,
        #     evaluation_groups[4]["count"] ,
        #     evaluation_groups[5]["count"] ,
        # ]  # クエリ結果に基づいて動的に設定

        labels = []
        values = []

        # グラフデータを設定（例: Django ORMのクエリ結果）
        # レビューカウント1件以上の場合は、データに加える
        for key, value in evaluation_groups.items():
            # print(f"キー: {key}, 星: {value['star']}, カウント: {value['count']}")
            if value['count'] > 0 :
                labels.append(value['star'])
                values.append(value['count'])

        # Matplotlibで円グラフを作成
        # 日本語フォントを指定（例: IPAexGothic）
        matplotlib.rcParams['font.family'] = 'IPAexGothic'
        plt.figure(figsize=(6, 6))
        plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=90, textprops={'fontsize': 18})
        plt.legend(fontsize=14, loc="upper right") # 凡例の設定
        plt.title("") # タイトル商品名を設定する
        plt.axis("equal")  # 円形を保つ

        # 画像をメモリに保存
        buffer = BytesIO()
        plt.savefig(buffer, format="png")
        buffer.seek(0)
        image_png = buffer.getvalue()
        buffer.close()

        # 画像をBase64エンコード
        graphic = base64.b64encode(image_png).decode("utf-8")

        # 結果をリストとして構築
        data = {
                    "data_item_nm": [obj.item_nm for obj in results] ,
                    "data_evaluation": [obj.evaluation for obj in results] ,
                    "chart": graphic
                }

        return JsonResponse(data)

    return JsonResponse({"error": "無効なリクエスト"}, status=400)

# class ModalDataView(View):
#     def get(self, request, *args, **kwargs):
        # template_name = 'modal_test.html'
        # record_id = kwargs.get('id')  # URLからIDを取得
        # try:
        #     record = ReviewModel.objects.get(id=record_id)
        #     data = {
        #         'item_name': record.item_nm,
        #         'review': record.review,
        #     }
        #     return JsonResponse(data)
        # except ReviewModel.DoesNotExist:
        #     return JsonResponse({'error': 'データが見つかりません'}, status=404)





