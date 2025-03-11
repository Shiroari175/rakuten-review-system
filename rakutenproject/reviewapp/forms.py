from email.policy import default

from django import forms

from .models import ReviewModel


class ReviewForm(forms.Form):
    name_rak_url = forms.URLField(
        label='楽天レビューURLを入力' ,
        widget=forms.URLInput(attrs={'class': ''}),
        max_length=1000 ,

    )
    name_rak_page = forms.IntegerField(
        label='取得するページ数' ,
        widget=forms.NumberInput(attrs={'class': 'form-label d-inline'}) ,
        min_value=1 ,
        max_value=50 ,
    )
