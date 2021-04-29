from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Article
from .forms import SearchForm
from .forms import ArticleForm

# 一覧
def index(request):
    # フォームデータを取得
    '''
    UserForm(request.GET)でGETメソッドで送られたフォームのデータを取得
    またrequest.GETによってそのままデータを受け取る
    '''
    searchForm = SearchForm(request.GET)
    '''
    is_validは、フォームに入力された値にエラーがないかをバリデートするメソッド
    例えば、IntegerFieldの項目に数値以外のものが入った場合や、必須の項目が空欄だった場合にエラーとなる
    '''
    if searchForm.is_valid():
        # 安全なデータを受け取る
        '''
        cleaned_dataは、バリデート後のデータを型に応じて一定のやり方で整形して返す
        例えば、DateFieldの項目に日付を文字列で入れたときに、常にdatetime.dateオブジェクトにしてくれる
        cleaned_dataを使うことで、その後の処理を行う際に自分でデータの整形をする手間が省ける
        is_valid() を呼び出して正常に検証されると(そして``is_valid()`` が True を返すと)、
        検証されたフォームデータは form.cleaned_data ディクショナリに格納される
        つまりis_valid()の結果がTrueのとき、form.cleaned_dataに情報が格納される。
        もっと言えばis_valid()を挟まないと入力データを参照することは出来ない。
        '''
        keyword = searchForm.cleaned_data['keyword']
        # 安全なデータを使ってオブジェクトを作成
        articles = Article.objects.filter(content__contains=keyword)
    else:
        # 最初にブラウザから呼び出されるときに使用するフォームクラスを指定
        searchForm = SearchForm()
        articles = Article.objects.all()

    context = {
        'message': 'Welcome my BBS',
        'articles': articles,
        'searchForm': searchForm
    }
    return render(request, 'polls/index.html', context)


# 詳細
def detail(request, id):
    article = get_object_or_404(Article, pk=id)
    context = {
        'message' : 'Show article' + str(id),
        'article' : article,
    }
    return render(request, 'polls/detail.html', context)


# 新規
def new(request):
    articleForm = ArticleForm()
    context = {
        'message' : 'New article.',
        'articleForm' : articleForm,
    }
    return render(request, 'polls/new.html', context)


# 作成
def create(request):
    if request.method == 'POST':
        articleForm = ArticleForm(request.POST)
        if articleForm.is_valid:
            article = articleForm.save()

    context = {
        'message': 'create article' + str(article.id),
        'article': article,
    }
    return render(request, 'polls/detail.html', context)


# 編集
def edit(request, id):
    return HttpResponse('Thais is edit. ' + str(id))

# 更新
def update(request, id):
    return HttpResponse('This is update. ' + str(id))

# 削除
def delete(request, id):
    article = get_object_or_404(Article, pk=id)
    article.delete()

    articles = Article.objects.all()
    context = {
        'message' : 'Delete article' + str(id),
        'articles' : articles,
    }
    return render(request, 'polls/index.html', context)
