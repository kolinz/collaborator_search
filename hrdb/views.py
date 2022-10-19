from contextlib import redirect_stdout
from django.shortcuts import render
# django.views.genericからTemplateView, ListView, CreateView, DetailView, DeleteViewをインポート
from django.views.generic import TemplateView, ListView, CreateView, DetailView, DeleteView
# モデルPersondataとCareerdataをインポート
from .models import Persondata, Resultdata
# PersondataFormとCareerdataForm をインポート
from .forms import PersondataForm, ResultdataForm
# アクセス制限のため、デコレータをインポート
from django.utils.decorators import method_decorator
# login_required をインポート
from django.contrib.auth.decorators import login_required
# django.urlsからreverse_lazyをインポート
from django.urls import reverse_lazy
# django.shortcutsから、リダイレクトと404エラー表示をインポート << 10月14日追記
from django.shortcuts import redirect, get_object_or_404 

# Create your views here.

class IndexView(ListView):
    '''トップページのビュー
    '''
    # idを降順に並べ替え
    model = Persondata
    quertset = Persondata.objects.order_by('posted_at')
    # index.htmlをレンダリング
    template_name = 'index.html'
    # 1ページあたりに表示するレコード数
    paginate_by = 9

# CreatePersonViewへのアクセスは、ログインユーザーに限定される。
@method_decorator(login_required, name='dispatch')
class CreatePersonView(CreateView):
    '''人物情報、新規登録ページのビュー
    '''
    # forms.pyのPersonDataFormをフォームクラスとして登録
    form_class = PersondataForm
    # レンダリングするテンプレート
    template_name = 'post_persondata.html'
    # フォームデータ投稿完了後のリダイレクト先
    success_url = reverse_lazy('hrdb:post_done')

    def form_valid(self,form):
        '''CreateViewクラスのform_validをオーバーライド
        フォームデータの登録を行う
        '''
        # 投稿ユーザーのidを取得して、モデルのauthorフィールドに追加するため、POSTされたデータを取得
        postdata = form.save(commit=False)
        postdata.author = self.request.user
        # 投稿データをデータベースに登録
        postdata.save()
        # スーパークラスのform_valid()の戻り値
        return super().form_valid(form)

class PostSuccessView(TemplateView):
    '''投稿完了ページのビュー
    '''
    # レンダリングするテンプレート
    template_name = 'post_success.html'

class DetailPersonView(DetailView):
    '''詳細ページのビュー
    
    投稿記事の詳細を表示するので、DetailViewを継承する
    Attributes:
      template_name: レンダリングするテンプレート
      model: モデルのクラス
    '''
  # テーブル連携としてモデルPersondataを設定
    model = Persondata
  # レコード情報をテンプレートに渡すオブジェクト
    context_object_name = "person_detail"
  # detail.htmlをレンダリングする
    template_name ='person_detail.html'

    # 10月14日 追記
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # テンプレートにコメント作成フォームを渡す
        context['resultcreate_form'] = ResultdataForm
        return context


class TitleView(ListView):
    '''肩書別表示のビュー
    Attributes:
    template_name: レンダリングするテンプレート
    paginate_by: 1ページに表示するレコードの件数
    '''
    # index.htmlをレンダリングする
    template_name ='index.html'
    # 1ページに表示するレコードの件数
    paginate_by = 9

    def get_queryset(self):
      '''クエリを実行する
      self.kwargsの取得が必要なため、クラス変数querysetではなく、get_queryset（）のオーバーライドによりクエリを実行する
      Returns:クエリによって取得されたレコード
      '''
      # self.kwargsでキーワードの辞書を取得し、
      # titleキーの値(titleテーブルのid)を取得
      title_id = self.kwargs['title']
      # filter(フィールド名=id)で絞り込む
      titles = Persondata.objects.filter(title=title_id).order_by('-posted_at')
      # クエリによって取得されたレコードを返す
      return titles


class OccupationView(ListView):
    '''職種別表示のビュー
    Attributes:
    template_name: レンダリングするテンプレート
    paginate_by: 1ページに表示するレコードの件数
    '''
    # index.htmlをレンダリングする
    template_name ='index.html'
    # 1ページに表示するレコードの件数
    paginate_by = 9

    def get_queryset(self):
      '''クエリを実行する
      self.kwargsの取得が必要なため、クラス変数querysetではなく、get_queryset（）のオーバーライドによりクエリを実行する
      Returns:クエリによって取得されたレコード
      '''
      # self.kwargsでキーワードの辞書を取得し、
      # occupationキーの値(Occupationテーブルのid)を取得
      occupation_id = self.kwargs['occupation']
      # filter(フィールド名=id)で絞り込む
      occupations = Persondata.objects.filter(occupation=occupation_id).order_by('-posted_at')
      # クエリによって取得されたレコードを返す
      return occupations


class OrgView(ListView):
    '''所属組織別表示ページのビュー
     Attributes:
     template_name: レンダリングするテンプレート
     paginate_by: 1ページに表示するレコードの件数
    '''
    # index.htmlをレンダリングする
    template_name ='index.html'
    # 1ページに表示するレコードの件数
    paginate_by = 9

    def get_queryset(self):
      '''クエリを実行する
      self.kwargsの取得が必要なため、get_queryset（）のオーバーライドによりクエリを実行する
      Returns:クエリによって取得されたレコード
      '''
      # self.kwargsでキーワードの辞書を取得し、
      # Orgキーの値(Orgテーブルのid)を取得
      org_id = self.kwargs['org']
      # filter(フィールド名=id)で絞り込む
      orgs = Persondata.objects.filter(org=org_id).order_by('-posted_at')
      # クエリによって取得されたレコードを返す
      return orgs


class ResultCreateView(CreateView):
  '''人物情報に対する、実績情報の登録ビュー
  '''
  model = Resultdata
  form_class = ResultdataForm
  
  def form_valid(self, form):
        post_pk = self.kwargs.get('pk')
        post = get_object_or_404(Persondata, pk=post_pk)

        newdata = form.save(commit=False)
        newdata.author = self.request.user
        newdata.persondata = Persondata.objects.get(id=self.kwargs['pk'])
        newdata.target = post
        newdata.save()

        return redirect('hrdb:person_detail', pk=post_pk)


class DetailMyPersonView(DetailView):
    '''詳細ページのビュー
    
    投稿記事の詳細を表示するので、DetailViewを継承する
    Attributes:
      template_name: レンダリングするテンプレート
      model: モデルのクラス
    '''
  # テーブル連携としてモデルPersondataを設定
    model = Persondata
  # レコード情報をテンプレートに渡すオブジェクト
    context_object_name = "myperson_detail"
  # detail.htmlをレンダリングする
    template_name ='myperson_detail.html'

    # 10月14日 追記
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # テンプレートにコメント作成フォームを渡す
        context['resultcreate_form'] = ResultdataForm
        return context


class MyPersonPageView(ListView):
    '''マイページのビュー
    '''
    # レンダリングするテンプレート
    template_name = 'mypage_person.html'
    # 1ページあたりに表示するレコード数
    paginate_by = 9

    def get_queryset(self):
      '''クエリを実行する
      self.kwargsの取得が必要なため、get_queryset（）のオーバーライドによりクエリを実行する
      Returns:クエリによって取得されたレコード
      '''
      queryset = Persondata.objects.filter(author=self.request.user).order_by('-posted_at')
      return queryset


class PersonDeleteView(DeleteView):
  '''レコードの削除を行うビュー
   Attributes:
   model: モデル
   temaplate_name: レンダリングするテンプレート
   success_url: 削除完了後のリダイレクト先のURL
  '''
  model = Persondata
  template_name = 'person_delete.html'
  success_url = reverse_lazy('hrdb:myperson_detail')

  def delete(self, request, *args, **kwargs):
      '''レコードの削除を行う
        Parameters:
        self: PersonDeleteViewオブジェクト
        request: WSGIRequest(HttpRequest)オブジェクト
        args: 引数として渡される辞書(dict)
        kwargs: キーワード付きの辞書(dict)
                {'pk': 21}のようにレコードのidが渡される
      
      Returns:
        HttpResponseRedirect(success_url)を返して
        success_urlにリダイレクト
      '''
      # スーパークラスのdelete()を実行
      return super().delete(request, *args, **kwargs)


class ResultDeleteView(DeleteView):
  '''レコードの削除を行うビュー
   Attributes:
   model: モデル
   temaplate_name: レンダリングするテンプレート
   success_url: 削除完了後のリダイレクト先のURL
  '''
  model = Resultdata
  template_name = 'result_delete.html'
  success_url = reverse_lazy('hrdb:mypage_person')

  def delete(self, request, *args, **kwargs):
      '''レコードの削除を行う
        Parameters:
        self: PersonDeleteViewオブジェクト
        request: WSGIRequest(HttpRequest)オブジェクト
        args: 引数として渡される辞書(dict)
        kwargs: キーワード付きの辞書(dict)
                {'pk': 21}のようにレコードのidが渡される
      
      Returns:
        HttpResponseRedirect(success_url)を返して
        success_urlにリダイレクト
      '''
      # スーパークラスのdelete()を実行
      return super().delete(request, *args, **kwargs)