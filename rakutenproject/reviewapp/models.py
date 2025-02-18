from django.db import models

from accounts.models import CustomUser

# 追加サンプル
# book = Book(title="Django入門", author="John Doe", published_date="2025-01-01")
# book.save()

# データ検索サンプル
# books = Book.objects.filter(author="John Doe")
# for book in books:
#     print(book.title)

# Create your models here.

class ReviewModel(models.Model) :
    """
    楽天レビュー保存モデル
    """
    # ユーザーテーブルとリレーション
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    haki_flg = models.IntegerField(default=0)
    item_nm = models.TextField()
    purchaser_nm = models.CharField(max_length=100)
    evaluation = models.IntegerField()
    review_title = models.CharField(max_length=100, null=True, blank=True)
    review_text = models.TextField()
    sex = models.CharField(max_length=5)
    age = models.CharField(max_length=10)
    item_detail = models.CharField(max_length=100)
    order_date = models.DateField(null=True, blank=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    # オプション指定
    class Meta:
        db_table = 'T_REVIEW' # テーブル名指定
        indexes = [
            models.Index(fields=['item_nm']),
            models.Index(fields=['review_text']),
        ]


