from django.contrib import admin
from .models import ReviewModel

# Register your models here.
# 管理画面よりDBを修正する設定
admin.site.register(ReviewModel)
