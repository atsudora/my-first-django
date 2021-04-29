from django import forms
from .models import Article

#forms.Formではフォーム要素の名前は自由に付けられる
class SearchForm(forms.Form):
    
    keyword = forms.CharField(label='検索', max_length=100) #フィールドを文字列型で定義

#データベースに書き込むためだけのフォーム
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields =('content', 'user_name')